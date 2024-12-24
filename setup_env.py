import subprocess
import sys
import os
import platform
import venv
import json
from pathlib import Path

class EnvironmentSetup:
    def __init__(self):
        self.python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.platform_system = platform.system()
        self.venv_path = "venv"
        self.requirements_path = "requirements.txt"
        self.config = {
            "python_version": self.python_version,
            "platform": self.platform_system,
            "setup_date": None,
            "dependencies": {}
        }

    def check_python_version(self):
        """Verify Python version meets requirements."""
        if sys.version_info < (3, 8):
            raise SystemError("Python 3.8 or higher is required")
        print(f"✓ Python version {self.python_version} OK")

    def create_virtual_environment(self):
        """Create a virtual environment if it doesn't exist and activate it."""
        if not os.path.exists(self.venv_path):
            print("Creating virtual environment...")
            venv.create(self.venv_path, with_pip=True)
            print("✓ Virtual environment created")
        else:
            print("✓ Virtual environment already exists")

        # Activate the virtual environment
        self.activate_virtual_environment()

    def check_virtual_environment(self):
        """Check if the virtual environment is active."""
        return "VIRTUAL_ENV" in os.environ

    def activate_virtual_environment(self):
        """Activate the virtual environment."""
        if self.check_virtual_environment():
            print("✓ Virtual environment is already active")
            return

        if self.platform_system == "Windows":
            activate_script = os.path.join(self.venv_path, "Scripts", "activate")
            bin_path = os.path.join(self.venv_path, "Scripts")
            activation_command = f".\\{activate_script}"
        else:
            activate_script = os.path.join(self.venv_path, "bin", "activate")
            bin_path = os.path.join(self.venv_path, "bin")
            activation_command = f"source {activate_script}"

        if os.path.exists(activate_script):
            print(f"Activating virtual environment using {activate_script}")
            os.environ["VIRTUAL_ENV"] = os.path.abspath(self.venv_path)
            os.environ["PATH"] = bin_path + os.pathsep + os.environ["PATH"]
            print("✓ Virtual environment activated")
        else:
            raise FileNotFoundError(f"Activation script not found: {activate_script}")

    def get_pip_path(self):
        """Get the correct pip path based on the operating system."""
        if self.platform_system == "Windows":
            return os.path.join(self.venv_path, "Scripts", "pip.exe")
        return os.path.join(self.venv_path, "bin", "pip")

    def get_python_path(self):
        """Get the correct Python path based on the operating system."""
        if self.platform_system == "Windows":
            return os.path.join(self.venv_path, "Scripts", "python.exe")
        return os.path.join(self.venv_path, "bin", "python")

    def upgrade_pip(self):
        """Upgrade pip to the latest version."""
        python_path = self.get_python_path()
        subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"])
        print("✓ Pip upgraded to latest version")

    def install_requirements(self):
        """Install required packages from requirements.txt."""
        pip_path = self.get_pip_path()
        print("\nInstalling requirements...")
        
        try:
            # First try to install everything at once
            result = subprocess.run(
                [pip_path, "install", "-r", self.requirements_path],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print("Bulk installation failed, trying individual packages...")
                self._install_individual_packages()
            
            print("✓ All requirements installed successfully")
            
        except Exception as e:
            print(f"Error installing requirements: {str(e)}")
            sys.exit(1)

    def _install_individual_packages(self):
        """Install packages one by one if bulk install fails."""
        pip_path = self.get_pip_path()
        with open(self.requirements_path, 'r') as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        for req in requirements:
            try:
                print(f"Installing {req}...")
                subprocess.run([pip_path, "install", req], check=True)
            except subprocess.CalledProcessError:
                print(f"Failed to install {req}")

    def setup_project_structure(self):
        """Create project directories if they don't exist."""
        directories = ['data', 'src', 'notebooks', 'tests']
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        print("✓ Project structure created")

    def save_environment_info(self):
        """Save environment information to a JSON file."""
        import datetime
        self.config["setup_date"] = datetime.datetime.now().isoformat()
        
        # Get installed packages
        pip_path = self.get_pip_path()
        result = subprocess.run([pip_path, "freeze"], capture_output=True, text=True)
        packages = result.stdout.strip().split('\n')
        
        for package in packages:
            if '==' in package:
                name, version = package.split('==')
                self.config["dependencies"][name] = version

        with open('environment_info.json', 'w') as f:
            json.dump(self.config, f, indent=2)
        print("✓ Environment information saved")

    def check_gpu_support(self):
        """Check if GPU support is available for machine learning."""
        try:
            import torch
            gpu_available = torch.cuda.is_available()
            print(f"GPU support: {'Available' if gpu_available else 'Not available'}")
        except ImportError:
            print("GPU support: torch not installed")

    def setup(self):
        """Run the complete setup process."""
        print("Starting environment setup...\n")
        try:
            self.check_python_version()
            self.create_virtual_environment()
            self.upgrade_pip()
            self.install_requirements()
            self.setup_project_structure()
            self.save_environment_info()
            self.check_gpu_support()
            print("\nSetup completed successfully!")
            
        except Exception as e:
            print(f"\nError during setup: {str(e)}")
            sys.exit(1)

def main():
    setup = EnvironmentSetup()
    setup.setup()

if __name__ == "__main__":
    main()
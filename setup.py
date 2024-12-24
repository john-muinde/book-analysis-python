import subprocess
import sys
import os

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        sys.exit(1)

def create_virtual_environment():
    """Create a virtual environment if it doesn't exist."""
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'])

def install_requirements():
    """Install required packages."""
    pip_cmd = 'venv/Scripts/pip' if os.name == 'nt' else 'venv/bin/pip'
    
    print("Installing required packages...")
    requirements = [
        'pandas>=2.2.0',
        'numpy>=1.26.0',
        'matplotlib>=3.8.0',
        'seaborn>=0.13.0',
        'scikit-learn>=1.4.0',
        'scipy>=1.12.0'
    ]
    
    with open('requirements.txt', 'w') as f:
        for req in requirements:
            f.write(f"{req}\n")
    
    subprocess.run([pip_cmd, 'install', '-r', 'requirements.txt'])

def setup_project_structure():
    """Create project directories if they don't exist."""
    directories = ['data', 'src', 'notebooks', 'tests']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def main():
    print("Setting up Book Analysis project...")
    check_python_version()
    create_virtual_environment()
    setup_project_structure()
    install_requirements()
    print("\nSetup complete! You can now run the analysis using: python main.py")

if __name__ == "__main__":
    main()
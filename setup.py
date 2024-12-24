import subprocess
import sys
import os

from setup_env import EnvironmentSetup

setup = EnvironmentSetup()

def setup_virtual_environment():
    # Create and run the environment setup
    setup.setup()

def setup_project_structure():
    """Create project directories if they don't exist."""
    print("Creating project structure...\n")
    directories = ['data', 'src', 'notebooks', 'tests']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("✓ Project structure created")

def main():
    print("Setting up Book Analysis project...")
    setup_project_structure()
    setup_virtual_environment()
    if not setup.check_virtual_environment():
        # Show activation instructions at the end
        print("\n=== IMPORTANT: Activate Your Virtual Environment ===")
        self.activate_virtual_environment()
    print("\n✓ Setup complete! You can now run the analysis using: python main.py")

if __name__ == "__main__":
    main()
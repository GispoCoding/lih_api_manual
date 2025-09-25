#!/usr/bin/env python3
"""
Quick setup script for the Location Information API Business Manual project.
This script helps team members set up their development environment quickly.
"""

import os
import sys
import subprocess
import platform

def run_command(command, shell=False):
    """Run a command and return success status."""
    try:
        result = subprocess.run(command, shell=shell, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {' '.join(command) if isinstance(command, list) else command}")
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"✗ {' '.join(command) if isinstance(command, list) else command}")
        print(f"  Error: {e.stderr}")
        return False, e.stderr

def main():
    """Main setup function."""
    print("🚀 Location API Business Manual - Setup Script")
    print("=" * 50)
    
    # Check Python version
    python_version = sys.version_info
    if python_version < (3, 8):
        print("❌ Python 3.8+ required. Current version:", sys.version)
        sys.exit(1)
    
    print(f"✓ Python {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # Detect OS
    os_name = platform.system()
    print(f"✓ Detected OS: {os_name}")
    
    # Check if virtual environment already exists
    if os.path.exists('venv'):
        print("⚠️  Virtual environment already exists. Remove 'venv' folder to recreate.")
        answer = input("Continue with existing environment? (y/n): ")
        if answer.lower() != 'y':
            print("Setup cancelled.")
            sys.exit(0)
    else:
        # Create virtual environment
        print("\n📦 Creating virtual environment...")
        success, _ = run_command([sys.executable, '-m', 'venv', 'venv'])
        if not success:
            print("❌ Failed to create virtual environment")
            sys.exit(1)
    
    # Determine activation script path
    if os_name == "Windows":
        activate_script = os.path.join('venv', 'Scripts', 'activate.bat')
        pip_path = os.path.join('venv', 'Scripts', 'pip')
    else:
        activate_script = os.path.join('venv', 'bin', 'activate')
        pip_path = os.path.join('venv', 'bin', 'pip')
    
    # Install requirements
    print("\n📚 Installing requirements...")
    success, _ = run_command([pip_path, 'install', '-r', 'requirements.txt'])
    if not success:
        print("❌ Failed to install requirements")
        sys.exit(1)
    
    # Test MkDocs installation
    print("\n🧪 Testing MkDocs installation...")
    mkdocs_path = os.path.join('venv', 'Scripts', 'mkdocs') if os_name == "Windows" else os.path.join('venv', 'bin', 'mkdocs')
    success, version_output = run_command([mkdocs_path, '--version'])
    if success:
        print(f"✓ {version_output.strip()}")
    
    # Success message
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    
    if os_name == "Windows":
        print("1. Activate environment: venv\\Scripts\\activate")
    else:
        print("1. Activate environment: source venv/bin/activate")
    
    print("2. Start development server: mkdocs serve")
    print("3. Open http://127.0.0.1:8000 in your browser")
    print("\nFor more information, see README.md")

if __name__ == "__main__":
    main()
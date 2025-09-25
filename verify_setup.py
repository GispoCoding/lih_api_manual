#!/usr/bin/env python3
"""
Verification script to check that the MkDocs environment is properly set up.
Run this script to validate your development environment.
"""

import os
import sys
import subprocess
import yaml

def check_item(description, condition, success_msg, error_msg):
    """Check a condition and print status."""
    print(f"{'✓' if condition else '✗'} {description}")
    if condition:
        if success_msg:
            print(f"  {success_msg}")
    else:
        if error_msg:
            print(f"  {error_msg}")
        return False
    return True

def main():
    """Main verification function."""
    print("🔍 Location API Business Manual - Environment Verification")
    print("=" * 60)
    
    all_good = True
    
    # Check Python version
    python_version = sys.version_info
    all_good &= check_item(
        "Python 3.8+ available",
        python_version >= (3, 8),
        f"Python {python_version.major}.{python_version.minor}.{python_version.micro}",
        f"Current version {python_version.major}.{python_version.minor} is too old"
    )
    
    # Check virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    all_good &= check_item(
        "Virtual environment active",
        in_venv,
        "Virtual environment is activated",
        "Please activate: source venv/bin/activate"
    )
    
    # Check MkDocs installation
    try:
        import mkdocs
        mkdocs_version = mkdocs.__version__
        all_good &= check_item(
            "MkDocs installed",
            True,
            f"MkDocs version {mkdocs_version}",
            None
        )
    except ImportError:
        all_good &= check_item(
            "MkDocs installed",
            False,
            None,
            "Run: pip install -r requirements.txt"
        )
    
    # Check MkDocs Material theme
    try:
        import material
        all_good &= check_item(
            "Material theme installed",
            True,
            "Material theme available",
            None
        )
    except ImportError:
        all_good &= check_item(
            "Material theme installed",
            False,
            None,
            "Run: pip install mkdocs-material"
        )
    
    # Check configuration file
    config_exists = os.path.exists('mkdocs.yml')
    all_good &= check_item(
        "mkdocs.yml exists",
        config_exists,
        "Configuration file found",
        "mkdocs.yml is missing"
    )
    
    # Validate YAML configuration
    if config_exists:
        try:
            with open('mkdocs.yml', 'r') as f:
                config = yaml.safe_load(f)
            all_good &= check_item(
                "mkdocs.yml is valid",
                True,
                f"Site name: {config.get('site_name', 'Not set')}",
                None
            )
        except Exception as e:
            all_good &= check_item(
                "mkdocs.yml is valid",
                False,
                None,
                f"YAML error: {e}"
            )
    
    # Check docs directory
    docs_exists = os.path.exists('docs') and os.path.isdir('docs')
    all_good &= check_item(
        "docs/ directory exists",
        docs_exists,
        f"Found {len(os.listdir('docs')) if docs_exists else 0} items in docs/",
        "docs/ directory missing"
    )
    
    # Check key content files
    key_files = ['docs/index.md', 'docs/glossary.md', 'docs/stylesheets/extra.css']
    for file_path in key_files:
        exists = os.path.exists(file_path)
        all_good &= check_item(
            f"{file_path} exists",
            exists,
            "Content file present" if exists else None,
            "Content file missing" if not exists else None
        )
    
    # Try building the site
    if all_good:
        print("\n🏗️  Testing site build...")
        try:
            result = subprocess.run(['mkdocs', 'build', '--quiet'], 
                                  capture_output=True, text=True, check=True)
            all_good &= check_item(
                "Site builds successfully",
                True,
                "Static site generated",
                None
            )
        except subprocess.CalledProcessError as e:
            all_good &= check_item(
                "Site builds successfully",
                False,
                None,
                f"Build error: {e.stderr}"
            )
    
    # Final status
    print("\n" + "=" * 60)
    if all_good:
        print("🎉 All checks passed! Your environment is ready.")
        print("\nNext steps:")
        print("1. Start development server: mkdocs serve")
        print("2. Open http://127.0.0.1:8000 in your browser")
        print("3. Edit content files in docs/ directory")
    else:
        print("❌ Some issues were found. Please fix them before proceeding.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
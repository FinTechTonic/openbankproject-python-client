#!/usr/bin/env python
"""
Script to build and test documentation locally.
This script helps ensure the documentation builds correctly before pushing to Read the Docs.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def clean_build():
    """Clean the build directory."""
    build_dir = Path("_build")
    if build_dir.exists():
        print("Cleaning build directory...")
        shutil.rmtree(build_dir)

def build_docs():
    """Build the documentation."""
    print("Building documentation...")
    try:
        # Get the project root directory (parent of docs directory)
        project_root = Path(__file__).parent.parent
        
        # Install documentation requirements from project root
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-e", 
            str(project_root) + "[docs]"
        ], check=True)
        
        # Build HTML documentation
        subprocess.run([
            sys.executable, "-m", "sphinx.cmd.build", 
            "-b", "html", ".", "_build/html"
        ], check=True)
        
        print("\nDocumentation built successfully!")
        print("You can view the documentation by opening _build/html/index.html in your web browser.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error building documentation: {e}")
        sys.exit(1)

def main():
    """Main function to build documentation."""
    # Change to the docs directory
    os.chdir(Path(__file__).parent)
    
    # Clean and build
    clean_build()
    build_docs()

if __name__ == "__main__":
    main() 
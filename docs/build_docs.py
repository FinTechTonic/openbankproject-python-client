#!/usr/bin/env python
"""
Script to clean, generate API docs, and build Sphinx documentation.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

def clean():
    """Remove _build and modules directories in docs."""
    docs_dir = Path(__file__).parent
    build_dir = docs_dir / "_build"
    modules_dir = docs_dir / "modules"
    for d in [build_dir, modules_dir]:
        if d.exists():
            print(f"Removing {d} ...")
            shutil.rmtree(d)

def generate_apidocs():
    """Run sphinx-apidoc to generate .rst files for all modules."""
    docs_dir = Path(__file__).parent
    project_root = docs_dir.parent
    modules_dir = docs_dir / "modules"
    print("Generating API docs with sphinx-apidoc ...")
    subprocess.run([
        sys.executable, "-m", "sphinx.ext.apidoc",
        "-o", str(modules_dir),
        str(project_root),
        "--separate", "--module-first", "--no-toc", "-f"
    ], check=True)

def build_html():
    """Build the HTML documentation."""
    docs_dir = Path(__file__).parent
    print("Building HTML documentation ...")
    subprocess.run([
        sys.executable, "-m", "sphinx.cmd.build",
        "-b", "html", str(docs_dir), str(docs_dir / "_build" / "html")
    ], check=True)

def main():
    os.chdir(Path(__file__).parent)
    clean()
    generate_apidocs()
    build_html()
    print("\nDocumentation built successfully! Open docs/_build/html/index.html in your browser.")

if __name__ == "__main__":
    main() 
from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openbankproject_client",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.30.0",
    ],
    extras_require={
        "docs": [
            "sphinx>=8.2.3",
            "sphinx-rtd-theme>=3.0.2",
        ],
    },
    python_requires=">=3.8",
    author="Joseph Pollack",
    author_email="joseph.pollack@emle.eu",
    description="Python client for the OpenBankProject API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FinTechTonic/openbankproject-python-client",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
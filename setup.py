"""
Setup configuration for Manga - Comprehensive Python Utilities Library
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="manga-lib",
    version="1.0.0",
    author="Manikandan",
    author_email="manikanda10407@gmail.com",
    description="A comprehensive open-source library with 5000+ utility functions for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Manikandan-777/manga",
    project_urls={
        "Bug Tracker": "https://github.com/Manikandan-777/manga/issues",
        "Documentation": "https://github.com/Manikandan-777/manga#readme",
        "Source Code": "https://github.com/Manikandan-777/manga",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=[],
    keywords=[
        "utilities",
        "library",
        "math",
        "string",
        "list",
        "dict",
        "algorithms",
        "data-structures",
        "validation",
        "helpers",
        "tools",
    ],
    zip_safe=False,
)

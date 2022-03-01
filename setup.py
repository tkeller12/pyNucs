import setuptools
from distutils.core import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("pyNucs/version.py", "r") as f:
    # Define __version__
    exec(f.read())

setup(
    name="pyNucs",
    packages=setuptools.find_packages(),
    version=__version__,
    license="MIT",
    description="Periodic Table of Magnetic Resonance Properties",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tim Keller",
    url="https://github.com/tkeller12/pyNucs",
    download_url="https://github.com/tkeller12/pyNucs",
    project_urls={
        "Source": "https://github.com/tkeller12/pyNucs"
    },
    keywords=["magnetic resonance nuclei nuclear spin"],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "PyQt5",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    entry_points=dict(
        console_scripts=[
            "hydrationGUI=pyNucs:main",
        ]
    ),
)

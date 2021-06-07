# import setuptools
import runpy

from setuptools import find_packages, setup

version_meta = runpy.run_path("./version.py")
VERSION = version_meta["__version__"]

with open("README.md", "r") as fh:
    long_description = fh.read()


def parse_requirements(filename):
    """
    Load requirements from a pip requirements file.
    """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name="wqxlib",
    version=VERSION,
    author="Jon Musselwhite",
    author_email="JMusselwhite@wvstateu.edu",
    description="A library to create files for the EPA's WQX service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlippingBinary/wqxlib/tree/main/wqxlib-python",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Hydrology",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)

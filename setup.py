from setuptools import setup, find_packages

setup(name="namegen",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        ],
    description="Name Generator",
    license="BSD",
    author="Amnon Grossman",
    author_email="emesh1@gmail.com",
    url="https://github.com/amnong/namegen",
    version="1.0.0",
    packages=find_packages(exclude=["tests"]),
    namespace_packages=["namegen"],
    )

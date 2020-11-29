import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('mendi/__init__.py', 'r').read(),
    re.M).group(1)


setuptools.setup(
    name='mendi',
    version=version,
    author="Aahnik Daw",
    author_email="meet.aahnik@gmail.com",
    description='Simple wrapper that helps you write a menu driven program easily.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aahnik/py-utility-pack",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)

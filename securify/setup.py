import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('securify/__init__.py', 'r').read(),
    re.M).group(1)


setuptools.setup(
    name='securify',
    version=version,
    author="Aahnik Daw",
    author_email="meet.aahnik@gmail.com",
    description='A minimal and secure command-line password manager.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aahnik/py-utility-pack",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires = ['python-dotenv','typer','rich','fernet'],
    zip_safe=False,
    entry_points={'console_scripts': [
        'securify=securify.cli:app',
    ], },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: WTFPL",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <4',

)

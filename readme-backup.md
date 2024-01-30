# pyospackage

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8365068.svg)](https://doi.org/10.5281/zenodo.8365068)
[![pyOpenSci](https://tinyurl.com/y22nb8up)](https://github.com/pyOpenSci/software-review/issues/115)

## What does pyospackage do?

pyosPackage is a demonstration pure Python package. It contains simple functions that perform basic addition. This
project is intended for anyone learning how to create a Python package. Or for anyone who just wants to understand a single way to create a Python package.

## How to install

You can install this package using either pip or conda-forge. We recommend that you create a new Python
environment to work in when installing this package. Use
whatever environment manager that you wish!

To install the package using pip:

`pip install pyospackage`

To install the package using conda-forge:

`conda install -c conda-forge pyospackage`

## Get started using packagename

To use this package:

```python
from pyospackage.add_numbers import add_num


a = add_num(1, 2)
print(a)

```

You can also add any links to this section to tutorials in your documentation.

## Community

Information here about contributing to your package. links to your code of conduct and development guide.

## How to cite packagename

citation information here
todo: create zenodo doi and add lesson on setting up zenodo for releases....


pypro backup


[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "pyosPackage"
#dynamic = ["version"]
version = "0.1.4" # uncomment this and comment the line above if you want to manually update versions
description = "A package that adds values together"
authors = [{ name = "Leah Wasser", email = "test@pyopensci.org" }]
maintainers = [{ name = "pyopensci community", email = "test@pyopensci.org" }]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3 :: Only",  # BE sure to specify that you use python 3.x
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
dependencies = ["pandas"] # Add your deps here
requires-python = ">=3.9" # important for pip to specify the minimum version of Python
readme = "README.md" # This will link to your readme file which is used populate your PyPI landing page
license = { text = "BSD-3" }

[project.urls] # Optional
"Homepage" = "https://www.pyopensci.org"
"Bug Reports" = "https://github.com/pyopensci/pyosPackage/issues"
"Source" = "https://github.com/pyopensci/pyosPackage/issues"
#"Funding" = "" # optional


[tool.hatch.envs.test]
dependencies = [
  "pytest"
]

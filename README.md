# pyOpenSci Demo Python Package -- pyospackage
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-7-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![PyPI - Version](https://img.shields.io/pypi/v/pyospackage)](https://pypi.org/project/pyospackage/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyospackage)](https://pypi.org/project/pyospackage)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10594121.svg)](https://doi.org/10.5281/zenodo.10594120)

## What does pyospackage do?
pyospackage is a demonstration Python package that compliments the pyOpenSci [beginner tutorial series on creating a Python package](https://www.pyopensci.org/python-package-guide/tutorials/intro.html).

## 🔧 About This Template

This package was built using [pyOpenSci’s Python package Copier template](https://github.com/pyOpenSci/pyos-package-template).l This template makes it easy for anyone to quickly create a Python package following best practices developed by the pyOpenSci community.

The template includes configuration for:
* [Standard Python package layout and structure](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html)
* [Code linting and formatting tools like Ruff](https://www.pyopensci.org/python-package-guide/package-structure-code/code-style-linting-format.html)
* [Setup for a test suite](https://www.pyopensci.org/python-package-guide/tests/index.html) 
* [Basic setup for Continuous Integration and Deployment (CI/CD)](https://www.pyopensci.org/python-package-guide/continuous-integration/ci.html)
* [Basic documentation infrastructure and files](https://www.pyopensci.org/python-package-guide/documentation/index.html) using mkdocs or sphinx

If you're interested in using the template, check out the [Copier Template Repo](https://github.com/pyOpenSci/pyos-package-template).


## 📘 Learn More About Python Packaging

This package accompanies our tutorials and docs on building and publishing high-quality Python packages:

- 📦 **Tutorial Series:** [Beginner Python Packaging Tutorials](https://www.pyopensci.org/python-package-guide/tutorials/index.html)
- 📖 **Overview:** [Python Packaging Overview](https://www.pyopensci.org/python-package-guide/overview.html)

These resources cover everything from package layout and versioning to testing, publishing to PyPI, and creating great documentation.

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## How to install

You can install this package using either pip or conda-forge. We recommend that you create a new Python
environment to work in when installing this package. Use
whatever environment manager that you wish!

To install the package using pip:

```shell
pip install pyospackage
```

To install the package using conda-forge:

```shell
conda install -c conda-forge pyospackage
```

## Get started using packagename

To use this package:

```python
from pyospackage.add_numbers import add_num


a = add_num(1, 2)
print(a)

```

You can also add any links to this section to tutorials in your documentation.

## Development

* TODO: link to development docs when they exist and move the text below to the
docs.

### Linting & Code Formatting

TODO: this will be added to the docs once they are created in a separate pr.

All linting and code formatting is implemented in this package using a combination
of pre-commit hooks and Ruff. Ruff is a fast, rust-based linter and code
formatter that covers functionality previously implemented by Black and isort
(formatters that are commonly used in the Python ecosystem). Ruff simplifies
your linting and code format setup but running all of the checks and fixes
using a single tool. As such pyOpenSci encourages new projects to consider
using Ruff.

## Community

Information here about contributing to your package. links to your code of conduct and development guide.

## How to cite pyospackage

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10594121.svg)](https://doi.org/10.5281/zenodo.10594121)

To cite pyospackage please follow the citation instructions on Zenodo.

```
Leah Wasser. (2024). pyOpenSci/pyosPackage: v0.1 Test release (v0.1.0). Zenodo. https://doi.org/10.5281/zenodo.10594121
```

## License

`pyospackage` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://batalex.github.io"><img src="https://avatars.githubusercontent.com/u/11004857?v=4?s=100" width="100px;" alt="Alex Batisse"/><br /><sub><b>Alex Batisse</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyosPackage/pulls?q=is%3Apr+reviewed-by%3ABatalex" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jon-e.net"><img src="https://avatars.githubusercontent.com/u/12961499?v=4?s=100" width="100px;" alt="Jonny Saunders"/><br /><sub><b>Jonny Saunders</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyosPackage/commits?author=sneakers-the-rat" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyosPackage/pulls?q=is%3Apr+reviewed-by%3Asneakers-the-rat" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.sckaiser.com"><img src="https://avatars.githubusercontent.com/u/6486256?v=4?s=100" width="100px;" alt="Sarah Kaiser"/><br /><sub><b>Sarah Kaiser</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyosPackage/commits?author=crazy4pi314" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyosPackage/pulls?q=is%3Apr+reviewed-by%3Acrazy4pi314" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://cimss.ssec.wisc.edu/"><img src="https://avatars.githubusercontent.com/u/3578659?v=4?s=100" width="100px;" alt="Geoff Cureton"/><br /><sub><b>Geoff Cureton</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyosPackage/commits?author=gpcureton" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyosPackage/pulls?q=is%3Apr+reviewed-by%3Agpcureton" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/steven-silvester-90318721/"><img src="https://avatars.githubusercontent.com/u/2096628?v=4?s=100" width="100px;" alt="Steven Silvester"/><br /><sub><b>Steven Silvester</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyosPackage/commits?author=blink1073" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyosPackage/pulls?q=is%3Apr+reviewed-by%3Ablink1073" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jameslamb"><img src="https://avatars.githubusercontent.com/u/7608904?v=4?s=100" width="100px;" alt="James Lamb"/><br /><sub><b>James Lamb</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyosPackage/commits?author=jameslamb" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyosPackage/pulls?q=is%3Apr+reviewed-by%3Ajameslamb" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/pyosPackage/commits?author=jameslamb" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/stevenrayhinojosa-gmail-com"><img src="https://avatars.githubusercontent.com/u/17886818?v=4?s=100" width="100px;" alt="steven"/><br /><sub><b>steven</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyosPackage/commits?author=stevenrayhinojosa-gmail-com" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

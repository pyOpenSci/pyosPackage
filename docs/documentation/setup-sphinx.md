# Sphinx documentation

This package uses Sphinx to create documentation.

We like sphinx because it is a community driven project with a community
driven theme that the scientific Python community works on:

`pydata_sphinx_theme`

:::{note}
MkDocs is the other most common documentation tool used in the Python
ecosystem.
:::

## Setup your documentation

You can chose to create sphinx documentation using sphinx-quickstart.
Below is the Sphinx-quickstart workflow used to create these docs. However,
inevitably you will likely customize the documentation setup. So you may also
want to just copy this repository's structure.

```
➜ sphinx-quickstart
Welcome to the Sphinx 5.3.0 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: n

The project name will occur in several places in the built documentation.
> Project name: pyosPackage
> Author name(s): pyOpenSci Community
> Project release []: 1.10

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: en
```

The `conf.py` file is the core that you use to configure your sphinx docs.
The conf.py file in this package is setup

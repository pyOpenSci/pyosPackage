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

```bash
➜ sphinx-quickstart
Welcome to the Sphinx 5.3.0 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: docs

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

## About the conf.py file

The `conf.py` file is what Sphinx uses to configure your documentation. This is
where you setup all of the features that you want your documentation to have.

:::{note}
Every tool and theme that you might use will have different configuration options
that will be placed in the `conf.py` file.
:::

:::{note}
You can remove the `make.bat` and `Makefile` files included with sphinx build.
In this package demo we use [Hatch environments and scripts](hatch-envs-scripts).
:::

## API / Reference documentation

It's useful to have a reference section in your docs that contains documentation
for your package's methods and classes. In this demo package we are using
[`sphinx-autoapi`](https://sphinx-autoapi.readthedocs.io/en/latest/index.html)
which will create these reference docs for you automatically. It's easy
to setup and creates nice-looking API docs without any needed setup.

`Sphinx-autoapi` is also customizable if you want to display things
differently.

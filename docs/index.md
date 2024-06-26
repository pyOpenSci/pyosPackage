# Welcome to pyosPackage's documentation

:::{toctree}
:maxdepth: 2
:hidden:
:caption: Contents:

home <self>
Hatch Scripts <hatch-envs-scripts>
Setup Sphinx <setup-sphinx>
:::

This documentation example uses myst as the primary documentation syntax.

:::{button-link} <https://www.pyopensci.org/python-package-guide/documentation/hosting-tools/myst-markdown-rst-doc-syntax.html>
:color: primary
:class: sd-rounded-pill float-left

Learn more about myst in our pyOpenSci packaging guide.

:::

Myst is a version of markdown that has more formatting flexibility.
This is what a sphinx directive looks like using myst markdown formatting:

```markdown
:::{toctree}
:maxdepth: 2
:caption: Contents:

```

If you see syntax like the syntax below, you are looking at rst.

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:
```

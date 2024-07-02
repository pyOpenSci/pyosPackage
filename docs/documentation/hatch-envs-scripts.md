# Hatch scripts and environments

* Hatch has a nox / tox / make like feature that allows you to:

1. Define `Python` environments with a set of tools that you wish to have installed.
2. Define commands that you wish to run in that environment.

All of the configuration for this goes into your `pyproject.toml` file.

## How to set this up

To set this up you first need to define an environment in your `pyproject.toml`
with all of the dependencies that the environment needs.

Below you can see we have defined an environment called `docs`.

:::{literalinclude} ../pyproject.toml
:language: toml
:start-at: [tool.hatch.envs.docs]
:end-before: [tool.hatch.envs.docs.scripts]
:::

Once you have an environment setup, you can then create commands that you wish
hatch to run for you within that environment. Below you setup two commands:

1. Build sphinx docs using the `sphinx-build` command.
2. Build sphinx docs in "live" mode which allows them to be updated every time
that you save

:::{literalinclude} ../pyproject.toml
:language: toml
:start-at: [tool.hatch.envs.docs.scripts]
:end-before: [tool.hatch.envs.test]
:::

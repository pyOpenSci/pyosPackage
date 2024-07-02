# Linting and Code Formatting

In our [packaging guide](https://www.pyopensci.org/python-package-guide/package-structure-code/code-style-linting-format.html), we
discuss various linters and code formatters used in the scientific Python
ecosystem, including tools like:

* [black](https://github.com/psf/black)
* [flake8](https://github.com/pycqa/flake8)
* [isort](https://pycqa.github.io/isort/)

[Ruff](https://github.com/charliermarsh/ruff) is a tool that has been
quickly becoming more popular. It is written in the Rust programming language
and is fast. We like Ruff because it can perform both code formatting
(similar to Black) and linting (similar to Flake8). This makes your setup
simpler.

## Running Linters with pre-commit

There are a few ways to call the linters when you are working on your code.

One option is to use pre-commit hooks. [pre-commit](https://pre-commit.com/)
runs any defined linters, code and text formatters, spellcheckers, and other
tools on your code locally when you use `git commit` to make a change. For
example:

```bash
git commit -m "message here"
```

By configuring pre-commit hooks, you can automatically run tools like Ruff and
codespell on your code and documentation every time you commit. This ensures
consistency and catches errors early.

While pre-commit is a powerful tool to add to your workflow, many do not like it:

* For beginner contributors, running pre-commit hooks can be confusing. You need
  to understand that each time you commit, it will run the checks. If it finds
  issues in your files, it will not actually commit your files to history. This
  can be confusing for even seasoned developers if they haven't used pre-commit
  before.
* Some prefer to set up autoformatters that run every time you save a file in
  your preferred code editor (like VSCode). More on that below.

## Pre-commit.ci Bot

The [pre-commit CI bot](https://pre-commit.ci/) integrates with your GitHub
repository to run pre-commit checks in an online continuous integration pipeline.
The bot will run any pre-commit hooks that you have set up on new pull requests
submitted to your repository.

Pre-commit.ci can be a nice tool to use for pull requests if set up correctly.
Ideally, you can set pre-commit CI to run only when you call it in a pull
request. This way, if you have a new contributor (or a seasoned one) who doesn't
want to set up pre-commit locally, or someone who wants to submit a pull request
(e.g., as a first contribution!) fully from the GitHub interface, you can enable
the bot to run pre-commit checks and fixes in the pull request yourself, as a
maintainer, before you merge the PR.

## Setting Up Autosave

TODO: More here on setting this up in VSCode and other tools.

# Setting Up Autosave for Ruff in VSCode and Spyder

## VSCode

1. Make sure you have the  the Python extension for vscode installed:

1. **Install Ruff:**
   Ensure you have Ruff installed in your environment. You can install it using pip:

   ```bash
   pip install ruff
   ```

1. Configure VSCode to run Ruff on save:

You can add this configuration to your workspace to ensure ruff is run on your
files every time you edit and save them.

```json
{
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.fixAll": "always",
            "source.organizeImports": "always",
        },
    },
    // TODO: figure out how the formatter is selected for notebooks
    "notebook.formatOnSave.enabled": true,
}
```

## Spyder

Autoformat with ruff is not yet a Spyder feature. See [this issue](https://github.com/spyder-ide/spyder/issues/21357) for discussions. 

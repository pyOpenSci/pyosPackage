# Below we grab the current date and time using python
# this is used to them support the copyright date always being the current year
# when you build your docs
import subprocess
from datetime import datetime

current_year = datetime.now().year
organization_name = "pyOpenSci"


project = "pyosPackage"
copyright = f"{current_year}, {organization_name}"
author = "pyOpenSci Community"

# *********** RELEASE NUMBER **************
# This is optional - if you want the release of your docs to align with your
# package release cycle then the code below will get the recent tag and use
# that to generate your documentation release value.
try:
    release_value = (
        subprocess.check_output(["git", "describe", "--tags"])
        .decode("utf-8")
        .strip()
    )
    release_value = release_value[:4]
except subprocess.CalledProcessError:
    release_value = "0.1"  # Default value in case there's no tag

# Update the release value
release = release_value


release = "1.10"

# -- General configuration ---------------------------------------------------
# Extensions add additional functionality to your documentation.
# TODO: describe each extension below
extensions = [
    # Autodoc will create API docs for you
    # "sphinx.ext.autodoc", # This is the older autodoc that doesn't support myst
    "autodoc2",  # Supports myst markdown, ugly output
    "autoapi.extension",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    # This allows you to create :::{todo} sections that will not be rendered
    # in the live docs
    "sphinx.ext.todo",
    "myst_parser",
]


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ****** setup MYST ******
# colon fence for card support in md
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
]
myst_heading_anchors = 3
myst_footnote_transition = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

# Autodoc
# autodoc2_render_plugin = "myst"
# autodoc2_packages = [
#     "../src/pyospackage",
# ]

autoapi_dirs = ["../src/pyospackage"]

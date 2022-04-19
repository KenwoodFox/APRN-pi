import subprocess

# Project Information
project = "APRN-Pi"
copyright = "2021-2022, To Be Announced"
author = "Kitsune Scientific"


# The full version, including alpha/beta/rc tags
repoProcess = subprocess.run(
    args=["git", "describe", "--dirty=-dirty", "--tags", "--always"],
    capture_output=True,
)

release = repoProcess.stdout.decode().strip()


# General Config
extensions = ["sphinx.ext.autosectionlabel", "sphinx.ext.imgconverter"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# HTML output options

html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# PDF output options

latex_elements = {"extraclassoptions": "openany,oneside"}

latex_logo = "resources/banner.png"

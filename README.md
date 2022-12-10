# Usage

This "cookie cutter" can help you get started creating your own OpenCDMS Plugin. First, make sure you have Python and [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) installed by following the instructions [here](https://cookiecutter.readthedocs.io/en/stable/installation.html).

You can then create your OpenCDMS plugin using the following command:

```
cookiecutter gh:opencdms-plugins/plugin-cookiecutter
```

# About

An OpenCDMS plugin is a group of one or more [OGC API Processes](https://docs.pygeoapi.io/en/latest/data-publishing/ogcapi-processes.html) contained in the `processes` directory and/or corresponding web components providing a user interface contained in the `components` directory. The name of plugins, processes and components should be prefixed with `opencdms_`.

OpenCDMS Plugins also contain user, administrator and developer documentation in `docs`, process and component tests and configuration. 

OpenCDMS Plugins have the potential to be used standalone or to be included in an OpenCDMS installation.

# Publishing plugins

Plugins can be published in Python Package Index ([PyPI](https://pypi.org/)) and/or Node Package Manager ([npm](https://www.npmjs.com/)). The Python package may include user interface code that can be used locally to interact with the Python process. However, the version published on npm should exclude the Python code as this is not useful to npm users.

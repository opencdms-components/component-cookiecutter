.. OpenCDMS Component cookiecutter documentation master file, created by
   sphinx-quickstart on Mon Jan  9 16:45:34 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

OpenCDMS Component cookiecutter documentation
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

An OpenCDMS Component is a code repository containing a collection of:

* Zero or more Python processes (`/processes`)
* Zero or more Web components (`/components`)
* Documentation (`/docs`)

Create your own OpenCDMS Component plugins using the component-cookiecutter `cookie cutter <https://cookiecutter.readthedocs.io/en/stable/>`_.

.. note::

   All processes in the collection share a common set of requirements and common test data.

   Python processes and Web components have shared documentation.

   Several processes may share a single common web componet for interacting with those processes.


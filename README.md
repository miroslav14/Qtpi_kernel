qtpi_kernel
===========

``qtpi_kernel`` is, an example of a modified Jupyter kernel python wrapper to 
enable inputs written in Qtpi quantum language. This repository complements the 
documentation on wrapper kernels here:  

http://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Installation
------------
To install ``qtpi_kernel`` from PyPI::

    pip install qtpi_kernel
    python -m qtpi_kernel.install

Using the Qtpi kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an Qtpi notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel qtpi`` to
their command line arguments.

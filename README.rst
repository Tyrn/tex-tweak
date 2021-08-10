TeX Tweaker
***********

Build and install
=================

::

    $ poetry build
    $ pip install dist/<...>.whl --user [-I]
    ...
    $ ttk --help

Use Git Hooks
=============

::

    $ pre-commit install
    ...
    $ pre-commit run --all-files

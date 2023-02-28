Theoretical Physics Reference
-----------------------------

This is an opensource book, available online at:

https://theoretical-physics.com

All files in the repository are licensed under the MIT license. The source code
of the repository is available at:

https://github.com/certik/theoretical-physics

Build
-----

Install prerequisites::

    sudo apt-get install python-sphinx texlive-fonts-recommended texlive-latex-extra texlive-fonts-extra dvipng

To build the book, do::

    make web

This builds both html and pdf versions, that you can find in the _build
directory.

Build Using Conda
-----------------

Conda build::

    mamba env create -f environment.yml
    conda activate tprbook
    make latex
    cd build/latex/
    tectonic *.tex

How to Push to Github
---------------------

First fetch the gh-pages branch and then use this script::

    ./copy-docs

and optionally push the gh-pages branch to github::

    git push github

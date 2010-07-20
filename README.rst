Theoretical Physics Reference
-----------------------------

This is an opensource book, available online at:

http://theoretical-physics.net/

All files in the repository are licensed under the MIT license. The source code
of the repository is available at:

http://github.com/certik/theoretical-physics

Build
-----

To build the book, do::

    make web

This builds both html and pdf versions, that you can find in the _build
directory.

How to Push to Github
---------------------

First fetch the gh-pages branch and then use this script::

    ./copy-docs

and optionally push the gh-pages branch to github::

    git push github

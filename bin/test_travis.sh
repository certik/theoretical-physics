#!/usr/bin/env bash

# Exit on error
set -e
# Echo each command
set -x

make latex
tectonic _build/latex/theoretical-physics.tex

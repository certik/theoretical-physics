#!/usr/bin/env bash

# Exit on error
set -e
# Echo each command
set -x

git clone https://github.com/mgieseki/dvisvgm
cd dvisvgm
./autogen.sh
./configure --enable-bundled-libs
make
sudo make install
cd ..

make web

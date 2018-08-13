#!/usr/bin/env bash

# Exit on error
set -e
# Echo each command
set -x

git clone https://github.com/mgieseki/dvisvgm
cd dvisvgm
git checkout 6001b3c0d5578f0647bf4cb9caaad0975a9e21d1
./autogen.sh
./configure --enable-bundled-libs
make
sudo make install
cd ..

make web

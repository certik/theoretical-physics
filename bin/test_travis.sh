#!/usr/bin/env bash

# Exit on error
set -e
# Echo each command
set -x

echo "Here is the token:"
echo "${GH_TOKEN} and Some other $GH_TOKEN stuff"
echo "Done."

#! /usr/bin/env bash

# This file automatically deploys changes to http://theoretical-physics.net/dev/
# This will happen only when a PR gets merged which is basically when a new
# commit is added to master. It requires an access token which should be
# present in .travis.yml file.
#
# Following is the procedure to get the access token:
#
# $ curl -X POST -u <github_username> -H "Content-Type: application/json" -d\
# "{\"scopes\":[\"public_repo\"],\"note\":\"token for pushing from travis\"}"\
# https://api.github.com/authorizations
#
# It'll give you a JSON response having a key called "token".
#
# $ gem install travis
# $ travis encrypt -r certik/theoretical-physics GH_TOKEN=<token> env.global
#
# This will give you an access token("secure"). This helps in creating an
# environment variable named GH_TOKEN while building.
#
# Add this secure code to .travis.yml as described here http://docs.travis-ci.com/user/encryption-keys/

# Exit on error
set -e
# Do *not* echo commands (so that we don't reveal GH_TOKEN)
set +x

ACTUAL_TRAVIS_JOB_NUMBER=`echo $TRAVIS_JOB_NUMBER| cut -d'.' -f 2`

if [[ "$TRAVIS_PULL_REQUEST" == "false" ]] && [[ "$ACTUAL_TRAVIS_JOB_NUMBER" == "1" ]] && [[ "$TRAVIS_BRANCH" == "master" ]]; then
        git config --global user.email "ondrej.certik@gmail.com"
        git config --global user.name "Automatic Deployment (Travis CI)"

        # New website:
        git clone https://${GH_TOKEN}@github.com/certik/tfc-deploy
        cd tfc-deploy
        rm -rf dev/
        cp -r ../_build/html/ dev/
        cp -r ../_build/html_mathjax/ dev/
        cp -r ../_build/latex/theoretical-physics.pdf dev/
        git add dev
        git commit -am "Deploy after building $TRAVIS_BUILD_NUMBER"
        git push -q origin master # -q hides the GH_TOKEN

        # Old website:
        git clone https://${GH_TOKEN}@github.com/certik/tfn-deploy
        cd tfn-deploy
        rm -rf dev/
        cp -r ../_build/html/ dev/
        cp -r ../_build/html_mathjax/ dev/
        cp -r ../_build/latex/theoretical-physics.pdf dev/
        git add dev
        git commit -am "Deploy after building $TRAVIS_BUILD_NUMBER"
        git push -q origin gh-pages # -q hides the GH_TOKEN
fi

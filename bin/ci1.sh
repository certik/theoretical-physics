#!/bin/bash

set -ex

if [[ ${GITHUB_REF} == 'refs/heads/master' ]]; then
    # Production
    bin/deploy.sh git@github.com:certik/tfc-deploy docs/dev
    echo "deploy_url=https://www.theoretical-physics.com/" >> $GITHUB_OUTPUT
else
    # Testing
    bin/deploy.sh git@gitlab.com:certik/tpr-test public/$GITHUB_REF_NAME
    echo "deploy_url=https://certik.gitlab.io/tpr-test/${GITHUB_REF_NAME}/" >> $GITHUB_OUTPUT
fi

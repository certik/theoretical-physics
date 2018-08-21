#! /usr/bin/env bash

set -e
set -x

dest_repo=$1
dest_dir=$2

if [[ "${dest_repo}" == "" ]]; then
    echo "Error: dest_repo is empty."
    exit 1
fi

if [[ "${dest_dir}" == "" ]]; then
    echo "Error: dest_dir is empty."
    exit 1
fi

if [[ "$3" == "stop" ]]; then
    dest_start="0"
else
    dest_start="1"
fi

mkdir ~/.ssh
chmod 700 ~/.ssh
ssh-keyscan gitlab.com >> ~/.ssh/known_hosts
ssh-keyscan github.com >> ~/.ssh/known_hosts
eval "$(ssh-agent -s)"
set +x
if [[ "${SSH_KEY}" == "" ]]; then
    echo "Error: SSH_KEY is empty."
    exit 1
fi
# Generate the private/public key pair using:
#
#     ssh-keygen -f deploy_key -N ""
#
# then set the $SSH_KEY environment variable in the GitLab-CI to the
# base64 encoded private key:
#
#     cat deploy_key | base64 -w0
#
# and add the public key `deploy_key.pub` into the target git repository (with
# write permissions).
ssh-add <(echo "$SSH_KEY" | base64 --decode)
set -x

git config --global user.email "ondrej.certik@gmail.com"
git config --global user.name "Automatic Deployment (GitLab-CI)"

git clone ${dest_repo} deploy
cd deploy
if [[ "${dest_start}" == "1" ]]; then
    rm -rf $dest_dir
    mkdir -p $dest_dir
    cp -r ../_build/html/* $dest_dir/
    cp -r ../_build/html_mathjax/ $dest_dir/
    cp -r ../_build/latex/theoretical-physics.pdf $dest_dir/
    git add $dest_dir
    COMMIT_MESSAGE="Deploy on $(date "+%Y-%m-%d %H:%M:%S")"
else
    git rm -r $dest_dir
    COMMIT_MESSAGE="Stop Deploy on $(date "+%Y-%m-%d %H:%M:%S")"
fi
git commit -m "${COMMIT_MESSAGE}"
git push origin master

#!/bin/bash
cwd=$PWD


submodulePaths=$(git submodule | awk '{$1=$1;print}' | cut -d ' ' -f 2)

function git_add_commit_update {
    nothing=$(git status | grep 'nothing to commit')
    if [[ -z $nothing ]]; then
        git add .
        git commit -m "Update Module"
        git push
    fi
}

for path in $submodulePaths
do
    cd $path
    detached_head=$(git branch | grep 'HEAD detached')
    echo $path
    if [[ -z $detached_head ]]; then
        git_add_commit_update
    else
        git stash
        git checkout master
        git stash pop
        git_add_commit_update
    fi
    cd $cwd
done
#!/bin/bash
cwd=$PWD


submodulePaths=$(git submodule | awk '{$1=$1;print}' | cut -d ' ' -f 2)

function git_add_commit_update {
    nothing=$(git status | grep 'nothing to commit')
    echo nothing $nothing
    if [[ -z $nothing ]]; then
        echo "nothing to commit for $PWD"
    else
        git add .
        git commit -m "Update Module"
        git push
    fi
}

for path in $submodulePaths
do
    cd $path
    detached_head=$(git branch | grep 'HEAD detached')
    if [[ -z $detached_head ]]; then
        git_add_commit_update
    else
        git stash
        git checkout master
        git stash pop
        git_add_commit_update
        # echo "Detached" $path
        # echo "Warn: have to be manually fixed"
    fi
    cd $cwd
done
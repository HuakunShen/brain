#!/bin/bash
cwd=$PWD


submodulePaths=$(git submodule | awk '{$1=$1;print}' | cut -d ' ' -f 2)

for path in $submodulePaths
do
    cd $path
    echo $path
    echo $(git branch)
    # if [[ -z $detached_head ]]; then
    # fi
    cd $cwd
done
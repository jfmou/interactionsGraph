#!/usr/bin/env bash

#export FLASK_ENV=dev

for file in tests/test_*.py;do
    if [ -e "$file" ];then
        echo "\033[32m+++ ${file}\033[0m"
        echo ""
        python "${file}" || exit 1
    fi
done

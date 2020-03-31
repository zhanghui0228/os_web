#!/bin/bash

module=(python-crontab, logzero, pyyaml)

for m in $module
do
    which pip3 >>/dev/null
    if [ $? -eq 0 ];then
        pip3 install $m
    else:
        pip install $m
    fi
done
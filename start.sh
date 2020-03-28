#!/bin/bash

# 启动命令
nohup python3 manage.py runserver 0.0.0.0:9000 >>log/run.log &
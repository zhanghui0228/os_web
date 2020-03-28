#!/bin/bash

nohup python3 manage.py runserver 0.0.0.0:9000 >>log/run.log &
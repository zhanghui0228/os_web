FROM docker.io/centos

COPY init.yaml /jiaolong/conf/
COPY base.py /usr/local/lib64/python3.6/site-packages/django/db/backends/mysql/base.py

RUN yum -y install python36.x86_64 git python3-devel gcc* \
    && pip3 install django python-crontab logzero pyyaml pymysql psutil requests \
    && echo "\033[32m 依赖安装完成！！\033[0m" \
    && git clone https://github.com/zhanghui0228/os_web.git /jiaolong/ \
    && echo "\033[32m 环境安装完成！！\033[0m" \
    && cd /jiaolong/ \
    && python3 /jiaolong/start.py \
    && echo "服务启动成功!!"

EXPOSE 9002
WORKDIR /jiaolong/
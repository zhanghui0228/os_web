import os
import psutil
from logzero import logfile, logger

try:
    if os.path.exists("log") == False:
        os.mkdir("log")
except Exception as err:
    print("创建日志目录失败,错误原因：{}".format(err))

logfile("log/system.log", maxBytes=3000000, backupCount=2, encoding="utf-8")

def useagent():
    cpu_list = []
    memory_list = []

    try:
        cpu_lv = psutil.cpu_percent()
        # cpu_list.append(cpu_lv)
        # logger.info("当前服务器cpu利用率{:.2f}%".format(cpu_lv))
        memory = psutil.virtual_memory()
        # print memory.used
        # print memory.total
        memory_lv = round(float(memory.used) / float(memory.total) * 100, 2)    # 保留两位小数
        # memory_list.append(memory_lv)
        # logger.info("当前服务器内存利用率{:.2f}%".format(memory_lv))
        local_info = [{
            "cpu": cpu_lv,
            "memory": memory_lv
        }]
        logger.info("信息获取如下：{}".format(local_info))
        return local_info[0]
    except Exception as err:
        logger.error("连接服务器异常：{}".format(err))
        return err


def local_system():
    local_sysname = os.uname().sysname
    local_release = os.uname().release
    local_machine = os.uname().machine
    local_info = [{
        "sysname": local_sysname,
        "release": local_release,
        "machine": local_machine
    }]
    try:
        logger.info("获取信息如下：{}".format(local_info))
        return local_info[0]
    except Exception as err:
        logger.error("获取信息失败：{}".format(err))
        return err


def local_disk():
    # 查询本地磁盘使用情况
    root_disk = psutil.disk_usage('/')
    disk_all_count = root_disk.total    # 根磁盘总大小
    disk_use_count = root_disk.used     # 根磁盘使用量
    disk_lv = root_disk.percent         # 根磁盘使用率
    local_info = [{
        "磁盘总大小": disk_all_count,
        "磁盘已使用": disk_use_count,
        "磁盘使用率": disk_lv
    }]
    try:
        logger.info("磁盘使用情况如下:{}".format(local_info))
        return local_info
    except Exception as err:
        logger.error("信息获取失败：{}".format(err))


# if __name__ == '__main__':
#     local_system()
#     useagent()
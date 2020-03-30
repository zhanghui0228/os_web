'''
 1、目前支持的检查范围 (本地信息)

 输出结果说明：
    return local_info[0]    [0] 输出为本地信息， 后面会增加多个内容，表示其它机器信息
'''
import os
import psutil
from logzero import logfile, logger, logging
from . import settings

log_path = os.path.join(settings.BASE_DIR, "log") 
try:
    if os.path.exists(log_path) == False:
        os.mkdir(log_path)
except Exception as err:
    print("创建日志目录失败,错误原因：{}".format(err))

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(moduls)s-%(processName)s-%(message)s')
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

        # 查询本地磁盘使用情况
        root_disk = psutil.disk_usage('/')
        disk_all_count = root_disk.total    # 根磁盘总大小
        disk_use_count = root_disk.used     # 根磁盘使用量
        disk_lv = root_disk.percent         # 根磁盘使用率

        local_info = [{
            "cpu": cpu_lv,
            "memory": memory_lv,
            "disk": disk_lv
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
        return local_info[0]
    except Exception as err:
        logger.error("信息获取失败：{}".format(err))


def local_service():
    name_list = []
    port_list = []
    service_list = []
    command_port = "netstat -tlnp | sed -n '3,$p' | awk '{print $4}' | awk -F':' '{print $NF}'"
    command_name = "netstat -ptln|grep -i listen|awk '{print $7}'|awk -F '[/]+'  '{print $2}'"
    line_port = os.popen(command_port).readlines()
    line_name = os.popen(command_name).readlines()

    # port
    for port in line_port:
        port = port.strip('\n')
        port_list.append(port)

    # server name
    for name in line_name:
        name = name.strip('\n')
        name_list.append(name)

    service_dict = {}
    for service in range(len(name_list)):
        service_dict[name_list[service]] = port_list[service]
        # service_dict[name_list[service]] = port_list[service]
    service_list.append(service_dict)

    # data['data'] = service_list
    # jsonStr = json.dumps(data, sort_keys=True, indent=4)
    local_info = service_list
        
    try:
        logger.info("服务端口如下：{}".format(local_info))
        return local_info[0]
    except Exception as err:
        logger.error("信息获取失败：{}".format(err))
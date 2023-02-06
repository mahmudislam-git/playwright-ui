# Importing the required libraries
import psutil
import GPUtil
import numpy as np
import matplotlib.pyplot as plt

# kb = float(1024)
# mb = float(kb ** 2)
# gb = float(kb ** 3)
#
# memTotal = int(psutil.virtual_memory()[0]/gb)
# memFree = int(psutil.virtual_memory()[1]/gb)
# memUsed = int(psutil.virtual_memory()[3]/gb)
# memPercent = int(memUsed/memTotal*100)
# storageTotal = int(psutil.disk_usage('/')[0]/gb)
# storageUsed = int(psutil.disk_usage('/')[1]/gb)
# storageFree = int(psutil.disk_usage('/')[2]/gb)
# storagePercent = int(storageUsed/storageTotal*100)
# #info = cpuinfo.get_cpu_info()['brand']

# def service():
#     print()
#     pidTotal = len(psutil.pids())
#     print("Running process: ", pidTotal)
#
# def load_avg():
#     print()
#     print('---------- Load Average ----------')
#     print()
#     print("Load avg (1 mins)  :",round(os.getloadavg()[0],2))
#     print("Load avg (5 mins)  :",round(os.getloadavg()[1],2))
#     print("Load avg (15 mins) :",round(os.getloadavg()[2],2))
#
# def system():
#     core = os.cpu_count()
#     host = socket.gethostname()
#     print()
#     print('---------- System Info ----------')
#     print()
#     print("Hostname     :",host)
#     print("System       :",platform.system(),platform.machine())
#     print("Kernel       :",platform.release())
#     print('Compiler     :', platform.python_compiler())
#     print('CPU          :',info, core,"(Core)")
#     print("Memory       :", memTotal,"GiB")
#     print("Disk         :", storageTotal,"GiB")
#
# def cpu():
#     print()
#     print('---------- CPU ----------')
#     print()
#     print("CPU Usage    : ",cpuUsage,"GiB")
#
# def memory():
#     print()
#     print('---------- RAM & Disk usage ----------')
#     print()
#     print("RAM Used         : ",memUsed,"GiB /",memTotal,"GiB","(",memPercent,"%",")")
#     print("Disk Used        : ",storageUsed,"GiB /",storageTotal,"GiB","(",storagePercent,"%",")")
#
# def network():
#     active = netifaces.gateways()['default'][netifaces.AF_INET][1]
#     speed = psutil.net_io_counters(pernic=False)
#     sent = speed[0]
#     psend = round(speed[2]/kb, 2)
#     precv = round(speed[3]/kb, 2)
#     print()
#     print('---------- Network stat ----------')
#     print()
#     print("Active interface : ",active)
#     print("Packet send      : ",psend,"KiB/s")
#     print("Packet receive   : ",precv,"KiB/s")

# def test_monitor_cpu_memory():
#     # service()
#     # system()
#     # load_avg()
#     # memory()
#     # network()
#
#     # # Getting % usage of virtual_memory ( 3rd field)
#     # print('RAM memory % used:', psutil.virtual_memory()[2])
#     # # Getting usage of virtual_memory in GB ( 4th field)
#     # print('RAM Used (GB):', psutil.virtual_memory()[3] / 1000000000)
#
#     # Getting all memory using os.popen()
#     total_memory, used_memory, free_memory = map(
#         int, os.popen('free -t -m').readlines()[-1].split()[1:])
#
#     # Memory usage
#     print("RAM memory % used:", round((used_memory / total_memory) * 100, 2))
#
#
#
#

# def test_monitor():
#     for i in range(100000000):
#         # Obtaining all the essential details
#         cpu_usage = psutil.cpu_percent()
#         mem_usage = psutil.virtual_memory().percent
#         print(cpu_usage)
#         print(mem_usage)
#         # Creating the scatter plot
#         plt.scatter(i, cpu_usage, color="red")
#         plt.scatter(i, mem_usage, color="blue")
#         plt.legend(["CPU", "Memory"], loc="lower right")
#         plt.pause(0.05)
#         # Obtaining the GPU details
#         GPUtil.showUtilization()
#     # Plotting the information
#     plt.show()
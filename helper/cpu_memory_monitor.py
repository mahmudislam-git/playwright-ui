from threading import Thread

import psutil
import GPUtil
import numpy as np
import matplotlib.pyplot as plt
import pytest


def monitor_cpu_memory():
    for i in range(100000000):
        # Obtaining all the essential details
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent
        print(cpu_usage)
        print(mem_usage)
        # Creating the scatter plot
        plt.scatter(i, cpu_usage, color="red")
        plt.scatter(i, mem_usage, color="blue")
        plt.legend(["CPU", "Memory"], loc="lower right")
        plt.pause(0.05)
        # Obtaining the GPU details
        GPUtil.showUtilization()
    # Plotting the information
    plt.show()

def start_monitor():
    thread = Thread(target=monitor_cpu_memory, args=())
    # thread.daemon = True
    thread.start()
    pytest.main()
    thread.join()
    print("start_monitor thread finished...exiting")
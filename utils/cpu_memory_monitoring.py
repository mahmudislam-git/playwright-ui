# Importing the required libraries
import psutil
import GPUtil
import numpy as np
import matplotlib.pyplot as plt
# Creating an almost infinite for loop to monitor the details continuously
for i in range(100000000):
    # Obtaining all the essential details
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    print(cpu_usage)
    print(mem_usage)
    # Creating the scatter plot
    plt.scatter(i, cpu_usage, color = "red")
    plt.scatter(i, mem_usage, color = "blue")
    plt.legend(["CPU", "Memory"], loc ="lower right")
    plt.pause(0.05)
    # Obtaining the GPU details
    GPUtil.showUtilization()
# Plotting the information
plt.show()
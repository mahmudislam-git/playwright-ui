# Importing the required libraries
import time
import psutil
import GPUtil
import matplotlib.pyplot as plt

pinfo = 0
while True:
    try:
        # Get Chromium Process ID
        processFlag = True
        while processFlag:
            for proc in psutil.process_iter():
                process = psutil.Process(proc.pid)
                if 'Chromium' in process.name():
                ##if proc.name() == 'Chromium':
                    try:
                        pinfo = proc.as_dict(attrs=['pid'])
                    except psutil.NoSuchProcess:
                        pass
                    else:
                        print('GET PROCESS ID of ', proc.name(), ' is ', pinfo['pid'])
                        processFlag = False
                        break
        # Get Current minutes second
        currentTime = time.strftime("%M:%S")

        # Get pid's memory and cpu usage
        pinfo_process = psutil.Process(pinfo['pid'])
        pinfo_mem_usage = pinfo_process.memory_percent()
        pinfo_cpu_usage = pinfo_process.cpu_percent(interval=0.5)

        # Get memory and cpu usage of system
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        # Plot the Graph
        # print(cpu_usage)
        # print(mem_usage)
        # Creating the scatter plot
        plt.scatter(currentTime, cpu_usage, color="red")
        plt.scatter(currentTime, mem_usage, color="blue")
        plt.scatter(currentTime, pinfo_mem_usage, color="green")
        plt.scatter(currentTime, pinfo_cpu_usage, color="yellow")
        plt.legend(["CPU", "Memory", "CHROMIUM_CPU", "CHROMIUM_Memory"], loc="lower right")
        plt.pause(0.05)
        # Obtaining the GPU details
        GPUtil.showUtilization()
    except KeyboardInterrupt:
        print("Program terminated mannaully")
        raise SystemExit
# Plotting the information
plt.show()

# Importing the required libraries

import psutil


for proc in psutil.process_iter():
    print('GET PROCESS ID of ', proc.name())

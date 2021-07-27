import time
from cpuinfo import get_cpu_info

print('Welcome to CpuChecker')
time.sleep(3)
print('An List of everything about your Cpu is gonna appear')
time.sleep(3)
for key, value in get_cpu_info().items():
    print("{0}: {1}".format(key, value))
    
        
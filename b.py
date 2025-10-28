import platform
from time import sleep
import os
import sys

module_list = []

speed = 0.1

def title():
    print("░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░")
    sleep(speed)
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░")
    sleep(speed)
    print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░")
    sleep(speed)
    print("░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ")
    sleep(speed)
    print("░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░")
    sleep(speed)
    print("░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░")
    sleep(speed)
    print("░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░")

def getsysinfo():
    import psutil

# Get virtual memory statistics
    memory_info = psutil.virtual_memory()

# Print detailed memory information
    print(f"TOT_RM: {round(memory_info.total / (1024**3), 2)} GB")
    print(f"AVA_RM: {round(memory_info.available / (1024**3), 2)} GB")
    print(f"USD_RM: {round(memory_info.used / (1024**3), 2)} GB")
    print(f"FRE_RM: {round(memory_info.free / (1024**3), 2)} GB")
    print(f"RAM Usage Percentage: {memory_info.percent}%")

    print(platform.machine())
    print(platform.version())
    print(platform.platform())
    print(platform.uname())
    print(platform.system())
    print(platform.processor())

def cls():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def getmodules():
    path_tv = "TV"
    path_audio = "AUD"
    if os.path.isdir(path_tv):
        print(f"'{path_tv}' is a directory.")
        module_list.append("TV")
    else:
        print(f"'{path_tv}' was not found")
        pass
    if os.path.isdir(path_audio):
        print(f"'{path_audio}' is a directory.")
        module_list.append(20)
    else:
        print(f"'{path_audio}' is not a directory.")
        pass
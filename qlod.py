print("QLOD")
import b
import subprocess

# 10 is TV, 20 is AUDIO TEST

if not b.module_list:
    print("List is empty, entering Terminal Enviorment.")

if len(b.module_list) > 1:
    print("List contains more than one value.")
    
else:
    print("List contains one value.")

if "TV" in b.module_list:
        subprocess.run(["python3", "TV/init.py"]) 
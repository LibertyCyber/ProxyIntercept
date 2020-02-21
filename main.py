#!/usr/bin/env python3
import time

#import my classes
from pull_config import Config
from Scaner import proxscan

#create base objects
config = Config('./config.json')

#init my configuration
config.read_conf()

#create variables
port = config.get_port()

print('''
            ____                        ___  _          ____                       
           / __ \____  ____ _____      |__ \( )_____   / __ \_________  _  ____  __
          / /_/ / __ \/ __ `/ __ \     __/ /|// ___/  / /_/ / ___/ __ \| |/_/ / / /
         / ____/ /_/ / /_/ / /_/ /    / __/  (__  )  / ____/ /  / /_/ />  </ /_/ / 
        /_/    \____/\__, /\____/____/____/ /____/  /_/   /_/   \____/_/|_|\__, /  
                    /____/     /_____/                                    /____/   
''')
print("[+]Starting ...")
time.sleep(0)

#create scanner
print("[+]Createing scanner ...")

try:
    scan = proxscan(port)
    print(f"[+]Scanner created on port {port}")
except:
    print("[-]Failed to create scanner")


print(scan.listen())
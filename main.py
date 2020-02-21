#!/usr/bin/env python3
from pull_config import Config

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
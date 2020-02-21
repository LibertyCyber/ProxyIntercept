#!/usr/bin/env python3
import json

class Config:

    def __init__(self,file):
        #arguments
        self.file = file
        self.content = None
        self.conf = None
    

    def read_conf(self):
        with open(self.file,'r')as fp:
            self.content = fp.read()
        
        self.conf = json.loads(str(self.content))

    def get_port(self):
        return(self.conf['port'])

    def path(self):
        return (self.file)
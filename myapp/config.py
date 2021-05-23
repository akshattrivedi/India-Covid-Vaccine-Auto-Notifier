"""
    Author: Akshat Trivedi
    Python Version: 3.9.2
"""

import json

class Config:
    __instance = None

    @staticmethod
    def getInstance():
        if Config.__instance == None:
            Config()
        
        return Config.__instance

    def __init__(self):
        if Config.__instance != None:
            raise Exception ("This is a Singleton Configuration Class!")
        else:
            Config.__instance = self
            self.data = json.load(open("myapp/config.json"))

configs = Config()
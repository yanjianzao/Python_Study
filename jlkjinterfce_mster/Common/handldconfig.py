import configparser
import os
#获取当前目录路径
cur_path = os.path.dirname(os.path.realpath(__file__))
class hand_config():
    def read_config(self,section_name,key_name,filename):
        self.con = configparser.ConfigParser()







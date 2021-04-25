import configparser
import os
#获取当前目录路径
cur_path = os.path.dirname(os.path.realpath(__file__))
class hand_config():
    def read_config(self,section_name,key_name,filename="config.ini"):
        self.con = configparser.ConfigParser()
        self.con.read(cur_path+'/'+filename, encoding='utf-8')
        self.dict_items = dict(self.con.items(section_name))
        return self.dict_items[key_name]
    def set_config(self,section_name,key_name,filename="config.ini",update_value=None,reset_section_name=None,**kwargs):
        self.read_config(section_name='App',key_name='token',filename="config.ini")
        if reset_section_name :
            self.con[reset_section_name] = {**kwargs}
        self.con.set(section_name, key_name,update_value)
        self.fo = open(filename, 'w', encoding='UTF-8')
        self.con.write(self.fo)
        self.fo.close()












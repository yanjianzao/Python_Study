import configparser
import os
#获取当前目录路径
cur_path = os.path.dirname(os.path.realpath(__file__))
class hand_config():
    def read_config(self,section_name,key_name,filename):
        self.con = configparser.ConfigParser()
        self.con.read(cur_path+'/'+filename, encoding='utf-8')
        self.dict_items = dict(self.con.items(section_name))
        return self.dict_items[key_name]

if __name__ == '__main__':
    hand = hand_config()
    print(hand.read_config(section_name='App',key_name='token',filename="config.ini"))










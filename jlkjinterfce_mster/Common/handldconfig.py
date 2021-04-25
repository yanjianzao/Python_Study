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
    def set_config(self,section_name,key_name,filename,update_value,reset_section_name=None,**kwargs):
        self.read_config(section_name='App',key_name='token',filename="config.ini")
        if reset_section_name :
            self.con[reset_section_name] = {**kwargs}
        self.con.set(section_name, key_name,update_value)
        self.fo = open(filename, 'w', encoding='UTF-8')
        self.con.write(self.fo)
        self.fo.close()
if __name__ == '__main__':
    hand = hand_config()
    hand.set_config(section_name='App',key_name='token',filename="config.ini",update_value='jksdhgiderisoghioer',reset_section_name='order',myarg2="xiaobei", myarg3=3)
    print(hand.read_config(section_name='App',key_name='token',filename="config.ini"))











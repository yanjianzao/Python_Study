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
    def set_config(self,section_name,key_name,filename,update_value):
        self.read_config(section_name='App',key_name='token',filename="config.ini")
        self.con['table'] = {'order_th': '订单号,申请人,状态', 'user_th': '用户名,权限,状态'}
        self.con.set('App', 'token', 'qwer1234')
        self.fo = open(filename, 'w', encoding='UTF-8')
        self.con.write(self.fo)
        self.fo.close()

if __name__ == '__main__':
    hand = hand_config()
    hand.set_config(section_name='App',key_name='token',filename="config.ini",update_value='jksdhgiderisoghioer')
    print(hand.read_config(section_name='App',key_name='token',filename="config.ini"))
'''
config['table'] = {'order_th': '订单号,申请人,状态', 'user_th': '用户名,权限,状态'}
config.set('App', 'token', 'qwer1234') #对section中的option进行设置
fo = open(path, 'w', encoding='UTF-8')  # 重新创建配置文件
config.write(fo)  # 数据写入配置文件
fo.close()
'''










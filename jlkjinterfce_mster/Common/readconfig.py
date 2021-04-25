import configparser
import os
#获取当前目录路径
cur_path = os.path.dirname(os.path.realpath(__file__))
def read_config(section_name,key_name,filename,update_value):
    con = configparser.ConfigParser()
    con.read(cur_path+'/'+filename, encoding='utf-8')
    # sections = con.sections()
    items = con.items(section_name)
    dict_items = dict(items)
    return dict_items[key_name]
    con1 = con.set(section_name,key_name,value=update_value)
    con1.write(open(filename, 'w'))
    new_value = con1.items(key_name)
    return new_value

if __name__ == '__main__':
    print(read_config(section_name='App',key_name='token',filename="config.ini",update_value='qwer1234'))




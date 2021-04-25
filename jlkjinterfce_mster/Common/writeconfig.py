from configparser import ConfigParser

path = 'config.ini'
config = ConfigParser()
# 对文件修改必须先将文件读取到config
config.read(path, encoding='UTF-8')
config['table'] = {'order_th': '订单号,申请人,状态', 'user_th': '用户名,权限,状态'}
config.set('App', 'token', 'qwer1234') #对section中的option进行设置
fo = open(path, 'w', encoding='UTF-8')  # 重新创建配置文件
config.write(fo)  # 数据写入配置文件
fo.close()

'''
[lang]
name=中文简体

[message]
applyLangTip           = 重启程序来应用更改。
runCommands            = 执行命令

[menu]
id               = 96
service          = 服务
help             = 帮助
officialSite     = 官网
officialHelp     = 帮助文档

[UI]
title          = 集成运行环境
stop           = 停止
startZentao    = 启动
account          = 账号
password         = 密码
'''
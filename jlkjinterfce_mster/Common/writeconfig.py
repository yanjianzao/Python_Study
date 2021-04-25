# 修改指定option的值
config.set('user', 'user_name', 'Mr L')
config.set('user', 'isRemember', 'True')
config.write(open(filename, 'w'))
# 重新查看修改后节点信息
items = config.items('user')
print(items)    # 结果 [('user_name', 'Mr L'), ('password', '222'), ('isremember', 'True')]
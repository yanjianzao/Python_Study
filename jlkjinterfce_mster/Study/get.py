import os,sys
sys.path.append(os.getcwd()) #os.getcwd() 方法用于返回当前工作目录
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
'''
os.path.dirname(path)	返回文件路径

'''
print(os.getcwd())

print(os.path.dirname(os.path.abspath(__file__)))

print(os.path.abspath(__file__))

import os

# 返回脚本绝对路径
print(os.path.abspath(__file__))

# 返回脚本上一层目录路径
root_path1 = os.path.dirname(os.path.abspath(__file__))
print(root_path1)

# 返回脚本上两层目录路径
root_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(root_path2)
import os
# 返回脚本的文件名称
print(os.path.basename(__file__))

'''

__file__表示显示文件当前的位置

但是：

如果当前文件包含在sys.path里面，那么，__file__返回一个相对路径！

如果当前文件不包含在sys.path里面，那么__file__返回一个绝对路径！


'''

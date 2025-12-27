# main.py
import sub

print(sub.sub1.os.getcwd())
print(sub.sub_sub.sub(1, 2))

import importlib
a = importlib.import_module('sub.sub1') # 绝对导入
b = importlib.import_module('sub1', package='sub') # 相对导入
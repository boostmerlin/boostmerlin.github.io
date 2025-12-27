# sub2.py

## sub2 导入同包内的sub1
# import sub1  # error: No module named 'sub1'
import sub.sub1 # ok,绝对导入
from . import sub1 # ok, 相对导入模块
from .sub1 import add # ok, 相对导入模块内的函数
print(add(1, 2))

## 导入子包sub_sub
from .sub_sub import sub_sub # o, 相对导入

## 导入上层的top
# from .. import top # error: attempted relative import beyond top-level package
# 但是如果把整个python-import作为一个包，由另外的模块来引用。这样..就不是一个顶层包，
# from .. import top就是合法的

import top # ok, 绝对导入
print("module sub2")
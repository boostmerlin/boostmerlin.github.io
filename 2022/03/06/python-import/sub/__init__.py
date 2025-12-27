# sub.__init__.py

from .sub_sub import sub_sub
from . import sub1

print("sub __init__.py")

def div(a, b):
    return a / b
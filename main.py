# -- file imports

# from utils import *  --- this is a bad practice
from utils import add, sub  # only import functions what you need and do not import everything if not necessary


print(add(10, 20))
print(sub(20, 10))


# lambda function

addition = lambda a, b: a + b
print(addition(100, 300))
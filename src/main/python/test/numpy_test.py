import numpy as np
import pandas as pd
l = [1,3,5,7,9] # 列表
arr = np.array(l) # 将列表转换为NumPy数组
print(arr) # 数据⼀样，NumPy数组的⽅法，功能更加强⼤
# 输出为
# array([1, 3, 5, 7, 9])

arr6 = np.random.randint(0,100,size = 10)

arr6.sort()

print(arr6)

arr1 = np.random.randint(0,100,size = (3,4,5))
print(arr1) # 输出 3

arr = np.random.randint(0,100,size = (3,4,5))
print(arr)
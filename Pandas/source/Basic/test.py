import pandas as pd

dict_data = {'a':1,'b':2 ,'c':3}
dict_data1 = [1,2,3]

sr = pd.Series(dict_data)

print(type(sr))
print('\n')

print(sr)
import pandas as pd

list_data = ['2019-01-02, 3.14', 'ABC', 100, True]
sr = pd.Series(list_data)

print(type(sr))
print(sr)
print('\n')

idx = sr.index
val = sr.values
print('tt')
print(idx)
print(val)

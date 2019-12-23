import pandas as pd

file_path = 'C:/Users/admin/Documents/PythonStudy0/Pandas/source/Csv/part2/read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1)
print('\n')

df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

df3 = pd.read_csv(file_path, index_col=None)
print(df3)

df4 = pd.read_csv(file_path, )
print(df4)
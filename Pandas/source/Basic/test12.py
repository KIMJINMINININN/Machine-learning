import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학': [90, 80, 70], 
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], 
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)

# df.set_index('이름', inplace=True)
print(df)
print('\n')

df.loc[3] = 0
print(df)
print('\n')

df.loc[4] = ['동규', 90, 80, 70, 60]
print(df)
print('\n')

df.loc['행5'] = df.loc[3]
print(df)
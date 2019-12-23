import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학': [90, 80, 70], 
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], 
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)

df.iloc[0][3] = 80
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준']['체육'] = 100
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 50
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)

df.loc['서준', ['음악', '체육']] = [90, 50]
print(df)

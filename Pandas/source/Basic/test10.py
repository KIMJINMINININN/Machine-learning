import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학': [90, 80, 70], 
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], 
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
print(df)
print('\n')

#변수에 저장을 해야 그다음 작업이 가능하다
a = df.loc['서준', '음악']
print(a)
b = df.iloc[0,2]
print(b)
print('\n')

#4가지는 같은것
c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0,[2,3]]
print(d)
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0, 2:]
print(f)
print('\n')

#4가지는 같은것
g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g)
h = df.iloc[[0,1], [2,3]]
print(h)
i = df.loc['서준':'우현', '음악':'체육']
print(i)
j = df.iloc[0:2,2:]
print(j)

df.loc['서준', '음악'] = 90
print(df)

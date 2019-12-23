import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학': [90, 80, 70], 
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], 
             '체육' : [100, 90, 90]}

# df.set_index('이름', inplace=True)
df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 데이터 프레임 df를 전치(메소드 활용)
df = df.transpose()
print(df)
print('\n')

# 데이터 프레임 df를 다시 전치
df = df.T
print(df)

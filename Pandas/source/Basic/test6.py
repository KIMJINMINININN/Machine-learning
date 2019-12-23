import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어' : [98, 89, 95],
            '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

df2 = df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')

df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True) #False가 되면 그냥 리턴이 된다. 원래 값이 변하지 않게된다
print(df3)

#Data를 지워주는 drop 메소드
#drop
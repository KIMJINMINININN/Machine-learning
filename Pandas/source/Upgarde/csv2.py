import pandas as pd

data = { 'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ['A', 'A+', 'B'],
        'basic' : ['C', 'B', 'B+'],
        'c++' : ['B+', 'C', 'C+'],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True) #name열을 인덱스로 지정
print(df)
#to_csv 메소드를 사용하여서 csv파일로 내보내기 파일명은 df_sample.csv로 저장
df.to_csv('./df_sample.csv')
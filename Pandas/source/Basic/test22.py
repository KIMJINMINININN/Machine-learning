import pandas as pd
# import numpy as np
import seaborn as sns

# titanic 데이터넷에서 age, far 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.tail()) # 마지막 5행 표시
print('\n')
print(type(df))
print('\n')

# 데이터 프레임에 숫자 10더하기
addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))
print('\n')

#데이터 프레임 끼리 연산하기
subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))


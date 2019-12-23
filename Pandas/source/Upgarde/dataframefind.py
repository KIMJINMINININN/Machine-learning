import pandas as pd

df = pd.read_csv('./part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.head())
print('\n')
print(df.tail())
#df의 모양과 크기 확인 튜플로 변환
print(df.shape)
print('\n')
# 데이터 프레임 df의 내용 확인
print(df.info())
print('\n')
# 데이터 프레임 df의 자료형 확인
print(df.dtypes)
print('\n')

#시리즈(열의) 자료형 확인
print(df.mpg.dtypes)
print('\n')

#기술통계 정보 확인
print(df.describe())
print('\n')
print(df.describe(include='all'))
# 데이터 프레임 df의 각 열이 가지고있는 원소 개수 확인
print(df.count())
print('\n')
# df.count()가 반환하는 객체 타입 출력 
print(type(df.count()))
print('\n')
# 데이터프레임 df의 특정 열이 가지고 잇는 고유값 확인 
unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')
# value_counts 메소드가 반호나하는 객체 타입 출력
print(type(unique_values))

#평균값
print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg', 'weight']].mean())

#중간값
print(df.median())
print('\n')
print(df['mpg'].median())

#최대값
print(df.max())
print('\n')
print(df['mpg'].max())

#최소값
print(df.min())
print('\n')
print(df['mpg'].min())

#표준편차
print(df.std())
print('\n')
print(df['mpg'].std())

#상관계수
print(df.corr())
print('\n')
print(df[['mpg','weight']].corr())



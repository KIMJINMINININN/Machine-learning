import pandas as pd

df = pd.DataFrame([[15,'남', '덕영중'], [17,'여', '수리중']],
                    index=['준서', '예은'],
                    columns=['나이', '성별', '힉교'])

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
print('\n')

df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '소속']

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
print('\n')

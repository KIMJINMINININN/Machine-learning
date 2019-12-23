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

# df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)
df1 = df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'})
#다시 새롭게 컬럼이나 index를 바꾸어줄때에는 rename이라는 메소드를 사용하여서
#새로운 변수에다가 입력을 해준다
print(df1)

df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '소속']

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
print('\n')


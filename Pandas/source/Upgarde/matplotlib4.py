# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('시도별 전출입 인구수.xlsx', fillna=0, header=0)
df = df.fillna(method='ffill')
df.head()
# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
#2가지의 방법은 같은 방법이다
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
df_seoul.head()

sr_one = df_seoul.loc['경기도']
#왜 index인데 values인지 인지를 할수있어야한다.
#중간의 type이 무엇인지 계속해서 확인하는 이유는 type에 따라서 어떤것을
#사용해야할지 나타나기 때문이다
plt.plot(sr_one.index, sr_one.values)
plt.plot(sr_one)
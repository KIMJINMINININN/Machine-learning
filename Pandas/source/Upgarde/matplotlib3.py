# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager
[f.name for f in matplotlib.font_manager.fontManager.ttflist if 'Nanum' in f.name]
[(f.name, f.fname) for f in matplotlib.font_manager.fontManager.ttflist if 'Nanum' in f.name]


#matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path ='/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('./part4/시도별 전출입 인구수.xlsx', fillna=0, header=0)
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

sr_one = df_seoul.loc['부산광역시']
#왜 index인데 values인지 인지를 할수있어야한다.
#중간의 type이 무엇인지 계속해서 확인하는 이유는 type에 따라서 어떤것을
#사용해야할지 나타나기 때문이다
plt.plot(sr_one.index, sr_one.values)
#차트 제목 추가
plt.title('서울 -> 부산 인구 이동')
#축 이름 추가
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.show()

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(sr_one, 'o', markersize=10)
ax2.plot(sr_one, marker='0', markerfacecolor='green', markersize=10, color='olive', linewidth=2, label='서울 -> 부산')
ax2.legend(loc='best')

ax1.set_ylim(50000,800000)
ax2.set_ylim(50000,800000)

ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)
plt.show()
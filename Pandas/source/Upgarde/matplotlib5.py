# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt

#matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path ='C:/Windows/Fonts/hmfmpyun.ttf'
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
# 서울에서 충청남도 경상북도 강원도 전라남도로 이동한 인구 데이터 값만 선택
col_years = list(map(str,range(1970,2018)))
df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

print(type(df_3))

df_3.head()

#스타일 서식 지정 
plt.style.use('ggplot')

# 그래프 객체 생성(figure에 1개의 서브 플롯을 생성)
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# axe 객체에 plot 함수로 그래프 출력
ax1.plot(col_years, df_3.loc['충청남도',:], marker='o', markerfacecolor='green', markersize=10, color='olive', linewidth=2,
       label='서울 -> 충남')
ax2.plot(col_years, df_3.loc['경상북도',:], marker='o', markerfacecolor='blue', markersize=10, color='skyblue', linewidth=2,
       label='서울 -> 경북')
ax3.plot(col_years, df_3.loc['강원도',:], marker='o', markerfacecolor='red', markersize=10, color='magenta', linewidth=2,
       label='서울 -> 강원')
ax4.plot(col_years, df_3.loc['전라남도',:], marker='o', markerfacecolor='yellow', markersize=10, color='yellow', linewidth=2,
       label='서울 -> 전남')

# 범례표시
ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')

# 차트 제목 추가
ax.set_title('서울 -> 충남, 경북, 강원, 전라 인구 이동', size=20)
ax.set_title('서울 -> 경북, 경북, 강원, 전라 인구 이동', size=20)
ax.set_title('서울 -> 강원, 경북, 강원, 전라 인구 이동', size=20)
ax.set_title('서울 -> 전남, 경북, 강원, 전라 인구 이동', size=20)

# 축 눈금 라벨 지정 및 90도 회전
ax1.set_xticklabels(col_years, rotation=20)
ax2.set_xticklabels(col_years, rotation=20)
ax3.set_xticklabels(col_years, rotation=20)
ax4.set_xticklabels(col_years, rotation=20)

plt.show()

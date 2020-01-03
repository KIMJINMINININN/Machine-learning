# 학습용 데이터
from sklearn import datasets
# 데이터를 학습용과 테스트용으로 나눌수있는 함수
from sklearn.model_selection import train_test_split
# 데이터 표준화
from sklearn.preprocessing import StandardScaler
# Perceptron 머신러닝을 위한 클래스
# from sklearn.linear_model import Perceptron
# 로지스트 회귀를 위한 클래스
# from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
# SVM을 위한 클래스
from sklearn.metrics import accuracy_score
# 파일 저장을 위해...
import pickle
import numpy as np

from plotdregion import *

names = None

def step1_get_data():
    # 아이리스 데이터 추출
    iris = datasets.load_iris()
    # print(iris)
    # 꽃 정보 데이터 추출
    X = iris.data[:150, [2,3]] #꽃잎 정보
    y = iris.target[:150] # 꽃 종류
    names = iris.target_names[:3] # 꽃 이름
    # print(X[0])
    # print(y[0])
    # print(names[0])
    return X, y

def step2_learing():
    X, y = step1_get_data()
    # 학습 데이터와 테스트 데이터로 나눈다.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    # 표준화 작업 : 데이터들을 표준 정규분포로 변환하여
    # 적은 학습횟수와 높은 학습 정확도를 갖기위해 하는 작업
    # test_szie = train과 test의 비율을 7:3으로 나타낸다
    sc = StandardScaler()
    # StandardScaler(X): 평균이 0과 표준편차가 1이 되도록 변환.
    # 데이터를 표준화한다.
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    # 학습한다.
    # ml = Perceptron(eta0=0.01, max_iter=40, random_state=0)
    ml = SVC(kernel='linear',C=0.1, random_state=0)
    # Logistic은 오버피팅이 잘일어나게된다 C=1000를 주어야 오버피팅이 잘일어나지 않게된다
    # C = 정규화 강도의 반대, 작은 값은 더 강한 정규화를 명시한다.
    # random_state = random 데이터 생성 시 seed of random number
    ml.fit(X_train_std, y_train)
    # 학습 정확도를 확인해본다
    X_test_std = sc.transform(X_test)
    y_pred = ml.predict(X_test_std)
    print("학습 정확도 : ", accuracy_score(y_test,y_pred))
    # 학습이 완료된 객체를 저장한다.
    with open('./ml.dat', 'wb') as fp:
        pickle.dump(sc, fp) # 
        pickle.dump(ml, fp) # 모델 
    print("학습 완료")
    
    # 시각화를 위한 작업
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined_std = np.hstack((y_train, y_test))
    plot_decision_region(X=X_combined_std, y=y_combined_std, classifier=ml, test_idx=range(70,100), title='perceptron')

def step3_using():
    # 학습이 완료된 객체를 복원한다.
    with open('./ml.dat', 'rb') as fp :
        sc = pickle.load(fp)
        ml = pickle.load(fp)
    X = [
        [1.4,0.2],[1.3,0.2],[1.5,0.2],
        [4.5,1.5],[4.1,1.0],[4.5,1.5],
        [5.2,2.0],[5.4,2.3],[5.1,1.8],
    ]
    X_std = sc.transform(X)
    # 데이터를 입력해 결과를 가져온다
    y_pred = ml.predict(X_std)

    for value in y_pred:
        if value == 0:
            print('Iris-setosa')
        elif value == 1:
            print('Iris-versicolor')
        elif value == 2:
            print('Iris-vppppppppp')

if __name__ == '__main__':
    step1_get_data()
    step2_learing()
    step3_using()

# step3_learing.py
from konlpy.tag import Okt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
import pickle
from time import time
import numpy as np


# 한글 형태소 분석을 위한 객체를 생성
okt = Okt()

def tokenizer(text):
    return okt.morphs(text)

# def tokenizer_nouns(text):
#     return okt.nouns(text)

# def word_tokenizer():
#     train_df = pd.read_csv('./10.NaverMoive/data/moive_train_dava.csv')
#     train_df['text_token'] = train_df['text'].apply(tokenizer_nouns)
#     print(train_df['text_token'])

def step3_learing():
    #데이터를 읽어온다
    train_df = pd.read_csv('./10.NaverMoive/data/moive_train_data.csv')
    test_df = pd.read_csv('./10.NaverMoive/data/moive_test_data.csv')

    # X_train = train_df['text'].astype('str').tolist() 다른방법
    X_train = train_df['text'].apply(lambda x: np.str_(x))
    y_train = train_df['star'].apply(lambda x: np.str_(x))

    X_test = test_df['text'].apply(lambda x: np.str_(x))
    y_test = test_df['star'].apply(lambda x: np.str_(x))
    # 학습을 위한 객체를 생성한다
    # vect = CountVectorizer()
    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer)
    logistic = LogisticRegression(C=10.0, penalty='l2', random_state=0)
    pipe = Pipeline([('tfidf', tfidf), ('clf', logistic)])
    #param_grid = [{'clf_c : [1,3.5,4.5,5.5,10]'}]
    #grid_cv = GridSearchCV(pipe, param_grid=param_grid, cv=3, scoring='accuracy', verbose=1)

    # 학습한다.
    stime = time()
    print('학습시작')
    pipe.fit(X_train, y_train)
    # grid_cv.fit(X_train, y_train)
    print('학습종료')
    etime = time()
    print('촐 학습시간 : %d' % (etime - stime))

    # 학습 정확도 측정
    y_pred = pipe.predict(X_test)
    print('정확도 : %.3f' % accuracy_score(y_test, y_pred))

    # 객체 저장
    with open('./pipe.dat', 'wb') as fp :
        pickle.dump(pipe, fp)

    print('저장완료')
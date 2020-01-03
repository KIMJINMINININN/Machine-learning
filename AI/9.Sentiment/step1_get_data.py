import pandas as pd
import os
import numpy as np
import codecs

def step1_get_data():
    # 데이터 파일들이 들어있는 경로
    path = './data/aclImdb/'
    print(path)
    # 긍정 또는 부정을 의미하는
    labels = {'pos':1, 'neg':0}
    # csv에 저장할 값을 관리할 객체
    df = pd.DataFrame()

    # 디렉토리 개수만큼 반복한다
    for s in('test', 'train'):
        for name in ('pos', 'neg'):
            # 읽어올 파일들이 들어있는 디렉토리명을만든다
            subpath = '%s/%s' % (s, name)
            dirpath = path + subpath
            # print(dirpath)

            # 현재 디렉토리 안에 잇는 파일 목록
            file_list = os.listdir(dirpath)
            # print(file_list)
            # 파일 목록을 순회하면서 정보를 가져온다.

            for file in file_list:
                fileName = os.path.join(dirpath, file)
                with codecs.open(fileName, 'r', 'utf-8') as fp :
                    txt = fp.read()
                    #print(labels[name], ":", txt)

                # DataFrame 객체에 저장한다
                df = df.append([[txt,labels[name]]], ignore_index=True)
                print(fileName)
    # 컬럼설정
    df.columns = ['review', 'sentiment']
    # 순서를 섞는다
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    # 저장한다.
    df.to_csv('./data/movie_review.csv', index=False)
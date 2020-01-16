import pickle
import numpy as np

def step4_using():
    #객체를 복원한다.
    with open('./pipe.dat', 'rb') as fp :
        pipe = pickle.load(fp)
    
    while True:
        text = input('리뷰를 작성해주세요')

        str1 = [text]
        # 예측 정확도
        r1 = np.max(pipe.predict_proba(str1) * 100)
        # 예측 결과
        r2 = pipe.predict(str1)[0]

        if r2 == '1':
            print('긍정적인 리뷰')
        else : 
            print('부정적인 리뷰')

        print('정확도 : %.3f' %r1)

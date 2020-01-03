import pickle
import numpy as np

def step5_using():
    # 객체를 복원한다
    with open('./data/pipe.dat', 'rb') as fp :
        pipeline = pickle.load(fp)

    while True : 
        text = input('영문으로 리뷰를 작성해주세요 : ')
        y = pipeline.predict([text])
        rate = pipeline.predict_proba([text]) * 100
        rate = np.max(rate)

        if y == 1:
            print('긍정적인 의견')
        else : 
            print('부정적인 의견')
        print('정확도 : %d' % rate)
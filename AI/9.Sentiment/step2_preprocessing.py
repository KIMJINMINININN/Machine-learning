import pandas as pd
import re
from time import time


def preprocessor(text):
    # 문자열의 내의 html 태그를 삭제한다.
    text = re.sub('<[^>*>]', '',text)
    # 문자열에서 이모티콘을 찾아낸다.
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)|\^.?\^', text)
    # 문장에서 특수문자를 제거하고
    # 문자열을 소문자로 변하고
    # 추출한 이모티콘을 붙혀준다
    text = re.sub('[\W]+', ' ', text.lower() + ' '.join(emoticons).replace('-', ''))
    # print(text)
    return text

def step2_preprocessing():
    # csv 데이터를 읽어온다.
    df = pd.read_csv('./data/movie_review.csv')

    # 전처리 작업
    stime = time()
    print('전처리 시작')
    df['review'] = df['review'].apply(preprocessor)
    print('전처리 완료')
    print('소요시간 : %d' % (time() - stime))

    # 전처리된 데이터를 저장한다.
    df.to_csv('./data/refined_moive_review.csv', index=False)
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk 

# stopword 단어 사전을 다운로드 받는다.
nltk.download('stopwords')
# stopword 데이터를 가져온다.
stop = stopwords.words('english')
# 단어 줄기를 하기위한 객체
porter = PorterStemmer()

# 공백으로 단어분리
def tokenizer(text):
    return text.split()

# 단어줄기
def tokenizer_porter(text):
    # 띄어쓰기를 기준으로 분리한다.
    word_list = text.split()
    # 단어 줄기 처리
    word_list2 = [porter.stem(word) for word in word_list]
    return word_list2

def step3_word_tokenizer():
    text = 'runners like running and thus they run'

    a1 = tokenizer(text)
    a2 = tokenizer_porter(text)
    print('a1:', a1)
    print('a2:', a2)
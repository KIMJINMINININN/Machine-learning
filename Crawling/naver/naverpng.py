import urllib.request
import os

url = 'https://fla.kr/ueJV'

dirname=os.path.dirname(__file__)
savename=dirname + '/test.jpg'
mem = urllib.request.urlopen(url).read()
print(savename)
with open(savename,mode='wb') as f:
    f.write(mem)
    print('저장되었습니다.')
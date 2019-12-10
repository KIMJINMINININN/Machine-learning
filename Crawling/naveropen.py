import requests
import pprint

client_id = 'sUy5IwdWl18vBftYeGPf'
ciient_secret = 'okf1O2UjrK'

naver_open_api = "https://openapi.naver.com/v1/search/shop.json?query=갤럭시노트10"
header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret" : ciient_secret}
res = requests.get(naver_open_api, headers=header_params)

if res.status_code == 200:
    data = res.json()
    for index, item in enumerate(data['items']):
        print (index + 1, item['title'], item['link'])
else:
    print("Error Code:",res.status_code)
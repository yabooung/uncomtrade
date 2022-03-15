from datetime import datetime, timedelta
from msvcrt import kbhit
from urllib import request
import json
import csv

# print(datetime.now().time())
# next_time = datetime.now()+ timedelta(hours=2)
# print(f'{next_time.hour}gogo')


import requests
import time

k = requests.get('http://www.naver.com')
if k.status_code != 200:
    print('응답완료')
print(k.url)
print(datetime.now())
# for i in range(1, 10):
#     print('시작')
#     if k.status_code == 200:
#         time.sleep(3)
#     print('브레이크뚫기')
# for i in range(1,10):
#     j = [i]
k = str(datetime.now())
print(k)
with open(f'hihi.json', 'w' ) as hihi:
    king = json.dump(k, hihi)


with open(f'./backup_10/count_10_10.json', 'r') as now:
    start = json.load(now)
excel_go = open(f'final.csv', 'w+',encoding='utf-8',newline='')
names= start[0]
wr = csv.DictWriter(excel_go, fieldnames=names)
wr.writerows(start)
import requests
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import pprint
import csv
import json
import time
import datetime


# ###
# ## 웹 페이지 가져오는 방법
# ###
# WEB_URL = 'https://comtrade.un.org/Data/' # 사용할 URL주소를 입력
# ###
# # urlib로 웹에 있는 소스 가져오기
# with urllib.request.urlopen(WEB_URL) as response:
#     html = response.read()
#     soup = BeautifulSoup(html,'html.parser')

# # request로 가져오기

# req = requests.get(WEB_URL)
# print(f'연결 상태 : {req.status_code}') ## 200뜨면 연결 성공
# # a= req.headers['content-type']
# # b=req.encoding
# # c=req.text
# # print(a,b,c)
# # print(soup)
# nations = open('nation.json', 'r',)
# nations_list = json.load(nations)
# BASE_URL = 'http://comtrade.un.org/api/get/?'
# URL = f'{BASE_URL}항목=변수&항목=변수'
# #항목=값& 형식으로 묶어주면 됌
# test_url = 'r=702&ps=2017&p=156&cc=01'

# data_list = []
# nations_code = nations_list.get('results')
# year = 2021
# nation = '042'
# cc = '0301'
# for nation in nations_code:
#     if nation.get('id') == 'all':
#         continue
#     code = nation.get('id')
#     change_data = f'max=502&type=C&freq=A&px=HS&ps={year}&r={code}&p=all&rg=1&cc={cc}'
#     req = requests.get(BASE_URL+change_data)
#     json_req = req.json()
#     extract = json_req['dataset']
#     data_list.append(extract)

# k = requests.get('https://comtrade.un.org/api/get?max=502&type=C&freq=A&px=HS&ps=2010&r=124&p=156&rg=all&cc=TOTAL&uitoken=2208cc78cb8c7966ccc2f62e74026724')

# pprint.pprint(k.json())

# change_data = 'max=502&type=C&freq=A&px=HS&ps=2021&r=842&p=all&rg=1&cc=0'
# req = requests.get(BASE_URL+test_url)
# req = requests.get('https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps=2021&r=all&p=0&rg=all&cc=TOTAL')

# print(json_req['dataset'])
# pprint.pprint(req.json())
# print(BASE_URL+test_url)
# pprint.pprint('https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps=2021&r=all&p=0&rg=all&cc=TOTAL')
# ex) /api/get?max=100000&type=C&freq=A&px=HS&ps=2017&r=702&p=156&rg=all&cc=01

# https://comtrade.un.org/data/doc/api/#DataRequests document
# ex) /api/get?max=502&type=C&freq=A&px=HS&ps=2018&r=410&p=579&rg=all&cc=030212%2C030213%2C030214
# type=C :상품조회하기 commodity
# freq=A : 연간 조회 
# ps : 연도(default == now)
# ps_list : https://comtrade.un.org/Data/cache/classificationHS.json
# px : classification (default values are HS for goods and EB02 for services) (분류 코드)
# r : reporter area (default == all) (조사 국가)
# r_list : https://comtrade.un.org/Data/cache/reporterAreas.json
# p : partner region (default == all) (상대 교역국가)
# p_list : https://comtrade.un.org/Data/cache/partnerAreas.json
# rg : trade flow (default == all) (수입인지 수출인지)
# rg_list : https://comtrade.un.org/Data/cache/tradeRegimes.json
# cc : HS (as reported) commodity codes 상품명 코드, 최대 5개까지가능 설정한 px에서 찾으면 됌

# 다큐보면 csv로 뽑는 법잇음

# /api/get?max=502&type=C&freq=A&px=HS&ps=2021&r=4&p=4&rg=all&cc=03
# result_data = extract
# file = open('sample.json', 'w+')
# file.write(json.dumps(result_data))

# with open('sample_test.csv','w', encoding='utf-8') as f:
#     excel = csv.writer(result_data)
#     excel.writeheader()
#     excel.writerows(result_data)

# print(extract)


# excel_go = open('test.csv', 'w',newline='')
# wr = csv.writer(excel_go)

# wr.writerow(data_list[0])
# for i in data_list:
#     wr.writerow(i.values())
# excel_go.close()


## 2번째 버전
# ps = ['2021%2c2020%2c2019%2c2018%2c2017',
#     '2016%2c2015%2c2014%2c2013%2c2012',
#     '2011%2c2010%2c2009%2c2008%2c2007',
#     '2006%2c2005'
#     ] #year
# r= [] # repoter
# p = [] #partner
# cc = ['03%2c0301%2c0302%2c0303%2c0304%2c0305',
#     '0306%2c0307%2c0308'
#     ] # code

# # %2c 분리기호

# # 나라 5개씩 가져오기 
# def get_nation(n=0):
#     nation_list = []
#     data = open('./nation_200.json', 'r')
#     data_list = json.load(data)
#     n = 0
#     for i in range(n, n+5):
#         nation_list.append(data_list['results'][i]['id'])
#     result = '%2c'.join(nation_list)
#     return result

# r= get_nation()
# p= get_nation()
# k = requests.get(f'https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps={ps[0]}&r={r}&p={p}&rg=1&cc={cc[0]}&uitoken=2208cc78cb8c7966ccc2f62e74026724')

# content = k.json()

# #요청한 데이터를 리스트로 모으기
# data_list = []
# extract = content['dataset']
# data_list.extend(extract)

# ## json으로 내보내서 저장하기
# with open ('./sample.json', 'w+') as outfile:
#     json.dump(data_list,outfile)

# ## 엑셀로 저장하기
# # with open('sample_test.csv','w', encoding='utf-8') as f:
# #     excel = csv.writer(content)
# #     excel.writeheader()
# #     excel.writerows(content)

# excel_go = open('test.csv', 'w',newline='')
# wr = csv.writer(excel_go)

# wr.writerow(data_list[0])
# for i in data_list:
#     wr.writerow(i.values())
# excel_go.close()

# 테스트
ps = ['2021%2c2020%2c2019%2c2018%2c2017',
    '2016%2c2015%2c2014%2c2013%2c2012',
    '2011%2c2010%2c2009%2c2008%2c2007',
    '2006%2c2005'
    ] #year
r= [] # repoter
p = [] #partner
cc = '03%2c0301%2c0302%2c0303%2c0304%2c0305%2c0306%2c0307%2c0308' # code

# %2c 분리기호

# 나라 5개씩 가져오기 
def get_nation(n=0,m='r'):
    nation_list = []
    if m=='r':
        data = open('./nation_200.json', 'r')
    else:
        data = open('./nation_report_197.json','r')
    data_list = json.load(data)
    if n != 0:
        n *= 5
    for i in range(n, n+5):
        try:
            nation_list.append(data_list['results'][i]['id'])
        except:
            pass
    result = '%2c'.join(nation_list)
    return result

#나라갯수조회
# data = open('./nation_200.json','r')
# data = open('./nation_report_197.json','r')
# data_list = json.load(data)
# countd=0
# for i in data_list['results']:
#     countd +=1
# print(countd)

#현재지점이 저장된 json을 불러옵니다
with open('./now.json', 'r') as now:
    start = json.load(now)

#요청한 데이터를 리스트로 모으기
data_list = []

# 나라는 총40번 돌리면됌
# 연도는 3번 돌리고
# 코드는 2번 돌리면 됩니다.
repoter_count = start['repoter_count']
count = start['count']
flow_time = start['flow_time']
print('for문시작')
for trying in range(start['year'],2): #year
    for repoter in range(start['repoter'],39): #repoter 194, 39번
        r = get_nation(repoter)
        for partner in range(start['partner'],40): #partner 197, 40번
            p = get_nation(partner,'p')
            k = requests.get(f'https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps={ps[trying]}&r={r}&p={p}&rg=1&cc={cc}&uitoken=2208cc78cb8c7966ccc2f62e74026724')
            # k = {'1':1, 'dataset':[{'11':11},{'22':22}]}
            content = k.json()
            extract = content['dataset']
            data_list.extend(extract)
            count +=1
            # print(f'https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps={ps[trying]}&r={r}&p={p}&rg=1&cc={cc}&uitoken=2208cc78cb8c7966ccc2f62e74026724')
            # 1번 돌때 마다 지점을 백업합니다
            s = {
                "year": trying,
                "repoter": repoter,
                "partner": partner,
                "count": count,
                "flow_time":flow_time,
                "repoter_count": repoter_count
            }
            with open('./now.json', 'w+') as file:
                file.write(json.dumps(s))
            print(f'돌아간 횟수 :{count} api주소:{k}')
            # 10번 마다 json으로 백업
            # json 저장
            if count % 10 == 0:
                with open (f'./count_10_{count}.json', 'w') as outfile:
                    json.dump(data_list,outfile)
                print(f'{count}번째 백업완료')
            
            # 100번지나면 저장하기
            if count % 100 == 0:
                print('100번 제한에 걸렸습니다.')
                print(f'{datetime.datetime.now().time()} 현재시각')
                next_time = datetime.datetime.now()+ datetime.timedelta(hours=1)
                print(f'{next_time.hour}에 시작할 수있습니다')

                # json 저장
                with open (f'./count_{count}.json', 'w') as outfile:
                    json.dump(data_list,outfile)
                print(f'second {count}번째 백업완료 ')

                # csv 저장
                excel_go = open(f'test{repoter_count}.csv', 'w',newline='')
                wr = csv.writer(excel_go)
                wr.writerow(data_list[0])
                for i in data_list:
                    wr.writerow(i.values())
                excel_go.close()
                print(f'{flow_time+1}번 저장하였습니다')
                time.sleep(3600)
                flow_time+=1
                print(f'{flow_time}번 돌았습니다.')

            # time.sleep(1)
        repoter_count+=1
print('for문끝')        

# for trying in range(3):
#     for repoter in range(40):
#         for partner in range(40):
#             for data_code in range(2):
#                 r = get_nation(repoter)
#                 p = get_nation(partner,'p')
#                 k = requests.get(f'https://comtrade.un.org/api/get?max=100000&type=C&freq=A&px=HS&ps={ps[trying]}&r={r}&p={p}&rg=1&cc={cc[data_code]}&uitoken=2208cc78cb8c7966ccc2f62e74026724')
#                 content = k.json()
#                 extract = content['dataset']
#                 data_list.extend(extract)

## json으로 내보내서 저장하기
with open ('./sample.json', 'w') as outfile:
    json.dump(data_list,outfile)

## 엑셀로 저장하기
# with open('sample_test.csv','w', encoding='utf-8') as f:
#     excel = csv.writer(content)
#     excel.writeheader()
#     excel.writerows(content)

# excel_go = open(f'final.csv', 'w+',newline='')
# wr = csv.writer(excel_go)

# wr.writerow(data_list[0])
# for i in data_list:
#     wr.writerow(i.values())
# excel_go.close()

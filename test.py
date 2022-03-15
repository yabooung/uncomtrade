from ast import dump
import csv
import json
import csv
for i in range(10,41,10):
    with open(f'./backup_10/count_10_{i}.json', 'r') as now:
        start = json.load(now)
    excel_go = open(f'final.csv', 'a',encoding='utf-8',newline='')
    names= start[0]
    wr = csv.DictWriter(excel_go, fieldnames=names)
    # if i == 10:
    #     wr.writerow(start[0])

    # for i in start:
    #     wr.writerow(i.values())

    wr.writeheader()
    wr.writerows(start)
excel_go.close()

# print(start['year'])

s = {
    "year": 8,
    "repoter": 0,
    "partner": 0,
    "count":0,
    "flow_time":0,
    "repoter_count": 1
}
# with open('./now.json', 'w+') as file:
#     file.write(json.dumps(s))
with open (f'./back/test_Test.json', 'w') as outfile:
    json.dump(s,outfile)
for i in range(1, 2):
    print(f'{i}번 입니다')

input()
import time
time.sleep(5)
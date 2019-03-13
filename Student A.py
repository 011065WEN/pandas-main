# #f=open('檔案名稱','檔案開始模式')
# file_path='123.txt'  #檔案路徑
# f=open(file_path,'r')  #開啟檔案
# fr=f.read()     #讀取檔案內容
# print(fr)       #印出內容
# f.close()               #關閉檔案
#
# #寫入檔案
# file_path='123.txt'  #檔案路徑
# f=open(file_path,'w')
# data=' GO GO GO' #資料內容
# f.write(data)
# f.close()
#
# #with代替f.close()
# file_path='123.txt'
# with open(file_path,'r')as f: #讀取
#     fr=f.read()
#     print(fr)

# import csv
# file_path='df.csv'
# with open(file_path,'r',encoding='utf-8') as csvfile: #Mac電腦編碼，問題，要轉Windows需加encoding='utf-8'
#     rows=csv.reader(csvfile)
#     for row in rows:
#         print(row)

#import csv
# file_path='df.csv'
# with open(file_path,'r',encoding='utf-8') as csvfile: #Mac電腦編碼，問題，要轉Windows需加encoding='utf-8'
#     rows=csv.DictReader(csvfile)  #使用dictation
#     for row in rows:
#         print(row)

#
# import csv
# members = [{'name': 'Kelsey'},
#         {'name': 'Van'},
#         {'name': 'WEN'}]
# with open('score.csv', 'w', newline='')as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['name', 'score'])  #writerow一次寫一列
#     for item in members:
#         writer.writerow([item['name']])

# #找出某一段錯誤並印出錯誤原因
# file_path='abc.txt'
# data=''
# try:
#     with open(file_path,'r')as f:
#         fr=f.read()
#         print(fr)
#         data=fr    #將讀入內容存入data
# except Exception as e:
#     print(e)
# print(data)

# #加入traceback追蹤是哪一行錯誤，並印出原因
import traceback
# file_path='abc.txt'
# data=''
# try:
#     with open(file_path,'r')as f:
#         fr=f.read()
#         print(fr)
#         data=fr    #將讀入內容存入data
# except:
#     traceback.print_exc()
# print(data)

import json
# members = [{'name': 'Kelsey'},
#         {'name': 'Van'},
#         {'name': 'WEN'}]
# obj=json.dumps(members)
# print(type(members))
# print(type(members[0]))
# print(obj)     #轉成json(用雙引號包住)
# print(type(obj))
#
# d=json.loads(obj)  #再轉回來(原本是用單引號)
# print(d)


# members = [{'name': '林'},
#         {'name': '雯'},
#         {'name': '儀'}]
# obj=json.dumps(members, ensure_ascii=False, indent=2) #顯示中文&一行一行顯示
# print(type(members))
# print(type(members[0]))
# print(obj)     #轉成json(用雙引號包住)
# print(type(obj))
#
# d=json.loads(obj)  #再轉回來(原本是用單引號)
# print(d)

from datetime import datetime
datestr='2019-03-12 20:00:00'
dt=datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S') #可以賞忘找json時間轉字串
print(dt)
print(type(dt))

import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')
dstr=dt.strftime('%H時')
dstr1=dt.strftime('%m/%d %H:%M')
print(dstr)
print(dstr1)
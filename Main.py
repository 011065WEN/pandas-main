import pandas as pd
import datetime
import os   #新增資料夾


dir = 'dataset'  #新增資料夾
os.makedirs(dir)   #新增資料夾

pd.set_option('display.width',200)
pd.set_option('display.max_columns',20)
df = pd.read_csv('nyc_taxi_sample.csv',encoding='utf-8')
df.describe()
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])  #將⽇日期字串串轉成datetime格式
datetime_value = df['pickup_datetime'].apply(lambda i:i.strftime('%Y-%m'))  #將 ‘2014-01-09 20:45:25’ 轉成 ‘2014-01’
datetime_uni = datetime_value.unique() #取得個日期

for item in datetime_uni:
    time = datetime.datetime.strptime(item,'%Y-%m') #datetime_uni內的項目為字串
    year = time.year  #取得年
    month = time.month  #取得月
    con = df['pickup_datetime'].dt.year == year  #條件一
    con1 = df['pickup_datetime'].dt.month == month  #條件二
    select = df[con & con1]  #選擇對應年、月的資料

    filename = dir + '/' + str(year) + '-' + str(month) + '.csv'  #檔案命名
    select.to_csv(filename , encoding='utf-8' , index=False)  #輸出檔案
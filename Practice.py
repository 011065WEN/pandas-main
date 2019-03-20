import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.width',200)
pd.set_option('display.max_columns',20)

df=pd.read_csv('dataset/2014-1.csv',encoding='utf-8')
df['pickup_datetime']=pd.to_datetime(df['pickup_datetime'])  #將⽇日期字串串轉成datetime格
#新增日期欄位
df['date'] = df['pickup_datetime'].dt.date

date_group = df.groupby('date')
print(df.head())
#查看每個組別的⼤小
date_group.size()
print(date_group.size())

#日期轉成星期 dayofweek取得星期
df['day of week'] = df['pickup_datetime'].dt.dayofweek
# Monday = 0, Sunday = 6
#依照欄欄位分組 groupby()
day_of_week_group = df.groupby('day of week')
#查看每個組別的⼤小
day_of_week_group.size().plot()
plt.show()

#日期轉成hour
df['hour'] = df['pickup_datetime'].dt.hour
# Monday = 0, Sunday = 6
#依照欄欄位分組 groupby()
hour_group = df.groupby('hour')
#查看每個組別的⼤小
hour_group.size().plot()
plt.show()
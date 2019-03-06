from MyMath import AddOperation as AddOpera
#函式基本語法 def定義
#def function_name(parameters):
    #do something
#    return something
#範例
# def add_x_and_y(x,y=4):
#     """
#     add x and y and return
#     :param x:
#     :param y:
#     :return:
#     """
#     sum0_num=x+y
#     return sum0_num
#定義xy位置 (不打東西可以先打pass，不然會出現紅色毛毛蟲~)
a = 10
b = 7
sum0=AddOpera.add_x_and_y(a,b)
print(sum0)
#在上面預設y=4,就算沒有定義y也會做計算
c=AddOpera.add_x_and_y(a)
print(c)
#變動數量的參數個數


def add_x_and_multi_y(x,*y): #第二個數字後都會被歸納為y
    """
    add x and multi y and return sum
    :param x: eg. 8
    :param y: eg. (6,9,4)
    :return:
    """
    #print(y) #(45,27,39,81)
    sum_num=x+sum(y)
    return sum_num #return 就是教函式吐東西出來
z=6
p=45
c=27
v=39
n=81
sum1=add_x_and_multi_y(z,p,c,v,b)
print(sum1)

sum2=add_x_and_multi_y(z,p,c,v,n,14,23)
print(sum2)

def add_x_and_y_return_multi_value(x,y):
    sum_num=x+y
    avg=sum_num/2
    return sum_num,avg
a=4
b=27
sum3,avg1=add_x_and_y_return_multi_value(a,b)
print(sum3)
print(avg1)

#匿名函式
#function_name=lambda para1,para2:do_something

#filter(判斷函式，要過濾的變數)
ls=[3,56,74,35,65,34,6,234,51]
def is_odd(x):
    return x % 2 == 1 #判斷除2取餘數是否等於1
result=filter(is_odd,ls)
f_list=list(filter(is_odd,ls))  #還要轉成字串
print(f_list)


#加入lambda省略 def
f_list=list(filter(lambda x:x % 2 ==1,ls))
print(f_list)

#模組
#import datetime


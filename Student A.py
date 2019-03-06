#machScores=[60,80,30,50,53,67,89,51,20]
#l=len(machScores)
#for i in range (0,l):
 #   print(i,machScores[i]*10)

#for item in machScores:
#    print(item)

#for each
#for item in machScores:
#    item=item*10
#    print(item)

#list comprehension\
##[item*10 for l in machScores]

#family={'dad':'Homer','mom':'Lisa'}
#for i,j in family.items():
#    print(i,j)

#x=(1,2,3)
#y=(4,5,6)
#z=(7,8,9)
#for x,y,z in zip(x,y,z):
#   print(x,y,z)

##tuple1=('a','b')
##for a,b in family.items():
##    print(a,b)

#machScores=[60,80,30,50,53,67,89,51,20]
#l=len(machScores)
#for i in range (0,l):
#   print(i,machScores[i]*10)
#ls=list(enumerate(machScores))
#print(ls)
#for index,item in enumerate(machScores):
#    print(index,item)

#當條件滿⾜足，則迴圈⼀一直執⾏行行
#count=0
#while count<10:
#    print(count)
#    count+=1

#當條件不滿⾜足，則執⾏行行else
#count=0
#while count<10:
#    print(count)
##else:
#    print('count>=10')

#for i in range(0,20):
#    if i % 2 == 1:
#        print(i)

#break
##mathScores=[60,80,30,50,53,67,89,51,20]
##for item in mathScores:
##    if item > 88:
##        break
##       print(item)


#continue
mathScores=[60,80,30,50,53,67,89,51,20]
for i in mathScores:
    if i >88:
        continue
    print(i)
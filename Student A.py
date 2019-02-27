mathscore=[34,2,18,95,47,37,65]
ls=['a','b','c']
print(mathscore+ls)

ls=[[1,4],[5,9]]
print(ls[1][1])
print(ls[0])

print(sorted(mathscore))

grade=[[5,14,7],[23,36,28],[88,80,92]]
print(grade[2])
print(sum(grade[0])/len(grade[0]))
print(sum(grade[1])/len(grade[2]))
print(sum(grade[2])/len(grade[2]))

#----Tuple
tuple3=('Lisa',23,'Female')
name,age,sex=tuple3
print(name,age,sex)
print(tuple3[0])
tuple4=('a','b')
print(tuple3+tuple4)

gradetuple=((5,14,7),(23,36,28),(88,80,92))
print(gradetuple)
mathtuple=gradetuple[2]
C=gradetuple[0]
E=gradetuple[1]
Cagv=sum(C)/len(C)
Eagv=sum(E)/len(E)
Magv=sum(mathtuple)/len(mathtuple)
print('Chinese Agv:',Cagv)
print('English Agv:',Eagv)
print('Math Agv:',Magv)
print(gradetuple+(94,90,96))
#---Dictionary
family={}
family['dad']='Homer'
print(family)
family['dad']='Andy'
print(family)

print(family.get('mom'))
family.update({'mom':'Lisa','son':'John'})
print(family)

GradeDict={'Cinnese':[5,14,7],'English':[23,36,28],'Math':[88,80,92]}
Mathscore=GradeDict['Math']
print(Mathscore)


#----Set


AllStudent={'John','Eva','Jill','Eric','Andy','Albert','Polina','Kristin','Angela'}
DanceClub={'Eric','Andy','Albert','Polina','Kristin'}
GuitarClub={'John','Eva','Jill','Eric','Andy'}
print(AllStudent)


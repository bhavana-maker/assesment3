def average(list):
 return sum(list)/len(list)
sname=input("enter student name=")
srollno=input("enter roll no=")
list=[]
num=int(input("how many numbers:"))
for n in range(num):
 numbers=int(input("enter number:"))
 list.append(numbers)
print("sum of elements in list:",sum(list))
average=average(list)
print("average of list=",round(average,2))
if(average>=80 and average<=100):
  print("grade=A")
elif(average>=60 and average<=79):
  print("grade=B")
elif(average>=50 and average<=59):
  print("grade=C")
elif(average>=40 and average<=49):
  print("grade=D")
else:
  print("fail")

list=[]
for i in range(1500,2701):
  if(i%7==0) and (i%5==0):
    list.append(i)
num= len(list)
for i in range(0,num):
  print(str(list[i])+" ")
print("press enter to escape")
input()
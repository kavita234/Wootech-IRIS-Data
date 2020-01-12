def maxNum(list):
  max=list[0]
  for a in list:
    if a > max:
      max=a
  return max
  
list= []
num = int(input("enter number of elements"))
for i in range(1,num+1):
  ele = int(input("enter element"))
  list.append(ele)
print("largest number is: ")
print(maxNum(list))
print("press enter to escape")
input()
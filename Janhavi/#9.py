def binarySearch(list,item):
  first=0
  last=len(list)-1
  found =False
  while (first<=last and not found):
    mid=(first+last)//2
    if(list[mid]==item):
      found=True
    else:
      if(list[mid] <item):
        first=mid+1
      else:
        last=mid-1
  return found
  
list=[]
num = int(input("enter number of elements"))
for i in range(1,num+1):
  ele = int(input("enter element"))
  list.append(ele)
item= int(input("enter number to be searched"))  
print(binarySearch(list,item))  
print("press enter to escape")
input()
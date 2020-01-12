def reverseString(s):
  r=''
  n=len(s)
  while n>0:
    r +=s[n-1]
    n=n-1
  return r  

s=input("enter string")
print(reverseString(s))
print("press enter to escape")
input()
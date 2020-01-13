import sys

inlist = []

while True:
	element = input("Enter list element:")
	if(not element):
		break
	inlist.append(element)

inlist.sort()
print("Largest number is:", inlist[-1])
	
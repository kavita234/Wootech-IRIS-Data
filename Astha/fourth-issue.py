def ordered_binary_search(arr, l, r, key):
	
	if r>=l:
		mid = int((l+r)/2)

		if key== arr[mid]:
			#Key found
			return True
		elif key < mid:
			#check on left side
			return ordered_binary_search(arr, l, mid-1, key)
		elif key > int((l+r)/2):
			#check on right side
			return ordered_binary_search(arr, mid+1, r, key)
	else:
		return False

#Test data given
arr = [0, 1, 3, 8, 14, 18, 19, 34, 52]
key = int(input("Enter key to search: "))
print(ordered_binary_search(arr, 0, len(arr)-1, key))
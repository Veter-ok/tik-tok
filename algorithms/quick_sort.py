def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[len(array) // 2]
		pivots = []
		less = []
		greater = []
		for i in array:
			if i < pivot:
				less.append(i)
			elif i > pivot:
				greater.append(i)
			else:
				pivots.append(i)
		return quicksort(less) + pivots + quicksort(greater)

arr = [4,1,6,3,9,8,2,5,7]

print(quicksort(arr))
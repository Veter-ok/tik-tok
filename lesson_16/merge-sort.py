def merge_list(a, b):
	i = j = 0
	c = []
	while i < len(a) and j < len(b):
		if a[i] <= b[j]:
			c.append(a[i])
			i += 1
		else:
			c.append(b[j])
			j += 1
	return c + a[i:] + b[j:]

def merge_sort(array):
	if len(array) < 2:
		return array
	middle = len(array) // 2
	left = merge_sort(array[:middle])
	right = merge_sort(array[middle:])
	return merge_list(left, right)

arr = [-2,3,7,1,-6,4,9,0,6]
print(*merge_sort(arr))
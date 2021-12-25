def insertion_sort(array):
	for i in range(1, len(array)):
		current = array[i]
		j = i - 1
		while j >= 0 and array[j] > current:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = current
	return array

nums = [1,3,8,2,4,6,9,5]
print(insertion_sort(nums))
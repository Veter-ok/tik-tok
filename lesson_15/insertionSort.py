from tqdm import tqdm
from random import randint


def insertion_sort(array):
	for i in tqdm(range(1, len(array))):
		current = array[i]
		j = i - 1
		while j >= 0 and array[j] > current:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = current
	return array

nums = [randint(1,20000) for _ in range(20000)]
print(insertion_sort(nums))
# tik-tok

Весь код из мего [тик тока](https://www.tiktok.com/@veter.ok77)
(1,500 - подписчиков)

____

### Binary Search (lesson_12)

```python
def bfs(graph, startPoint, endPoint):
	visited = []
	search_queue = graph[startPoint]
	next_point = 0
	queues = len(graph[startPoint])
	level = 1
	while len(search_queue) > 0:
		point = search_queue[0]
		queues -= 1
		del search_queue[0]
		if point not in visited:
			if point == endPoint:
				return endPoint, level
			else:
				search_queue += graph[point]
				next_point += len(graph[point])
				if queues == 0:
					queues = next_point
					next_point = 0
					level += 1
				visited.append(point)
		print(point, level, queues, search_queue)
	return False
```

### Quicksort (lesson_14)

``` python
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
```

### Breadth-first Search (lesson_17)

```python
def bfs(graph, startPoint, endPoint):
	visited = []
	search_queue = graph[startPoint]
	next_point = 0
	queues = len(graph[startPoint])
	level = 1
	while len(search_queue) > 0:
		point = search_queue[0]
		queues -= 1
		del search_queue[0]
		if point not in visited:
			if point == endPoint:
				return endPoint, level
			else:
				search_queue += graph[point]
				next_point += len(graph[point])
				if queues == 0:
					queues = next_point
					next_point = 0
					level += 1
				visited.append(point)
		print(point, level, queues, search_queue)
	return False
```

graph = [
	[0, 2, float("inf"), 3, 1, 10],
	[2, 0, 4, float("inf"), float("inf"), float("inf")],
	[float("inf"), 4, 0, float("inf"), float("inf"), 3],
	[3, float("inf"), float("inf"), 0, float("inf"), 8],
	[1, float("inf"), float("inf"), float("inf"), 0, 6],
	[10, float("inf"), 3, 8, 6, 0]
]

def floyd(graph, start, end):
	n = len(graph)
	mid_graph = [[j for j in range(n)] for _ in range(n)]
	for k in range(n):
		for i in range(n):
			for j in range(n):
				d = graph[i][k] + graph[k][j]
				if graph[i][j] > d:
					graph[i][j] = d
					mid_graph[i][j] = k
	path = [end]
	while start != end:
		end = mid_graph[end][start]
		path.append(end)
	return path

print(floyd(graph, 0, 5))
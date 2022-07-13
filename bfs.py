graphF = {
	"А": ["Б","В","Г"],
	"Б": ["Е"],
	"В": ["Е","Д","Ж"],
	"Г": ["Ж","З"],
	"Д": ["Е"],
	"Е": ["Ж","К"],
	"Ж": ["К"],
	"З": ["К"],
	"К": []
}

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

print(bfs(graphF, "А", "К"))
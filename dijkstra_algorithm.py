graph = {
	"A": {"B": 1},
	"B": {"C": 4, "D": 2, "E": 8},
	"C": {"B":4, "E": 4},
	"D": {"B": 2, "E": 4},
	"E": {"B": 8, "C": 4},
}
costs = {
	"B": 1,
	"C": float("inf"), 
	"D": float("inf"),
	"E": float("inf")
}
processed = []

def find_lowest_cost_node(costs):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node


def find_lowest_way(graph, endPoint):
	node = find_lowest_cost_node(graph["A"])
	while node is not None:
		cost = costs[node]
		neigbords = graph[node]
		for n in neigbords.keys():
			new_cost = cost + neigbords[n]
			if costs[n] > new_cost:
				costs[n] = new_cost
		processed.append(node)
		node = find_lowest_cost_node(graph[node])
	return costs[endPoint]


print(find_lowest_way(graph, "E"))
# Author: Dinh-Mao Bui, Anh-Tu Nguyen
# Rule of traversing: Alphabetical ordered, then left to right,
# Points: 2
def traverse(tree, init):
	queue = [init]
	traversed = []
	while queue:
		'''
			Student fixes the loopy path from here to the end of this function
		'''
		node = queue.pop(0)
		if not traversed:
			traversed.append(node)
		#traversed.append(node)
		leaves = tree[node]
		for leaf in leaves:
			if leaf not in traversed:
				traversed.append(leaf)
				#print(traversed[-1])
				queue.append(leaf)
				#print("not in", leaf)
	return traversed


# Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [[init]]
	if init == goal:
		return "No kidding, pls"
	while queue:
		'''
			You implement the path finder from here
		'''
		dist1 = queue.pop(0)
		node = dist1[-1]
		if node not in traversed:
			leaves = tree[node]
			for leaf in leaves:
				dist2 = list(dist1)
				dist2.append(leaf)
				queue.append(dist2)
				if goal == leaf:
					return dist2
			traversed.append(node)
	# break
	return "No such path exists"

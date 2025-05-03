def bfs(graph, startNode):
    visited=[]
    queue=[]

    visited.append(startNode)
    queue.append(startNode)

    while queue:
        current = queue.pop(0)
        for neighbors in graph[current]:
            if neighbors not in visited:
                visited.append(neighbors)
                queue.append(neighbors)

    print(visited)


n= int(input("Enter the number of node: "))
graph={}

for _ in range(n):
    node = input("Node Name: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node]=neighbors

source = input("Enter the source node for BFS traversal: ")

print('\nBFS Traversal:')
bfs(graph, source)
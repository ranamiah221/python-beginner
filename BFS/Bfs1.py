graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited=[]
queue=[]

def bfs(visited, graph, startNode):
    visited.append(startNode)
    queue.append(startNode)

    while queue:
        print(queue)
        m=queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

bfs(visited, graph, '5')    
import collections
def bfs(graph, root):
    visited=set()
    queue = collections.deque([root])
    
    while queue:
        vertex=queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)
  
    
graph={
    0: [1,3],
    1: [0,4],
    3: [0,4],
    4: [1,3,5],
    5: [3,4,6],
    6: [5]
}
bfs(graph, 6)


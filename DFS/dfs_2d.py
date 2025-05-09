def isValid(grid, visited, i, j):
    row=len(grid)
    col=len(grid[0])
    if i<0 or j<0 or i>=row or j>=col or visited[i][j]==1:
        return False
    return True

def dfs(grid, visited, start):
    i, j = start[0],start[1]
    print(grid[i][j], end=" ")
    visited[i][j]=1
    if isValid(grid,visited,i,j+1):
        dfs(grid,visited,(i, j+1))

    if isValid(grid,visited,i,j-1):
        dfs(grid,visited,(i, j-1))

    if isValid(grid,visited,i+1,j):
        dfs(grid,visited,(i+1, j))

    if isValid(grid,visited,i-1,j):
        dfs(grid,visited,(i-1, j))

grid=[
    [3,1,5],
    [7,8,2],
    [14,11,9]
    ]

row=len(grid)
col=len(grid[0])

visited=[]
for _ in range(row):
    temp=[]
    for _ in range(col):
        temp.append(0)
    visited.append(temp)
for item in visited:
    print(item)

dfs(grid, visited,(0,2))
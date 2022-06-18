# most-general guide
# bfs : queue 
# dfs : recursion. iterative stack
# graph : adjancency list. visited set().
# matrix : 4-directions
# binary tree : root, left, right

### all graphs
# https://leetcode.com/discuss/study-guide/1326900/graph-algorithms-problems-to-practice
# Dijkstra's algorithm: Is an algorithm for finding the shortest paths between nodes in a graph, which may represent, for example, road networks
# Union–find data structure or disjoint-set data structure or merge–find set, is a data structure that stores a collection of disjoint (non-overlapping) sets. Equivalently, it stores a partition of a set into disjoint subsets.
# minimum spanning tree (MST) : is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
# Topological sort : is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
# Bellman Ford : Is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.
# Floyd Warshall : Is an algorithm for finding shortest paths in a directed weighted graph with positive or negative edge weights.
# Eulearian Path : Is an algorithm that finds a path that uses every edge in a graph only once.

# graph build graph
def buildGraph() : 
    adjList = {i:[] for i in range(n)}
    for start, end in edges:
        adjList[start].append(end)
        adjList[end].append(start)

# graph bfs 
# https://leetcode.com/problems/clone-graph/discuss/494246/Python-Simple-BFS-and-DFS-with-detailed-explanation

# graph dfs recursion or stack
# https://leetcode.com/problems/clone-graph/discuss/494246/Python-Simple-BFS-and-DFS-with-detailed-explanation

    

# matrix bfs 
def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        row, col = len(grid), len(grid[0])
        islands = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    q = collections.deque([(i, j)])
                    grid[i][j] = '2'

                    while q:
                        x, y = q.popleft()
                        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                            xx, yy = x+dx, y+dy
                            if 0 <= xx and 0 <= yy and xx < row and yy < col and grid[xx][yy] == '1':
                                q.append((xx, yy))
                                grid[xx][yy] = '2'
                    islands += 1            
        return islands

# matrix dfs
class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for row, col in lst:
            if row>=0 and col>=0 and row<len(grid) and col<len(grid[row]) and grid[row][col] == "1" :
                self.dfs(grid, row, col)
    
        
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    islands +=1
        return islands

# matrix stack
def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):    
                if (r,c) in visited or grid[r][c] == '0':
                    continue	
                islands += 1
                stack = [(r,c)]  
                while stack:       
                    newR, newY = stack.pop()        
                    if 0 <= newR < len(grid) and 0 <= newY < len(grid[0]) and grid[newR][newY] == '1' and (newR,newY) not in visited:
                        visited.add((newR,newY))
                        stack.append((newR+1,newY))
                        stack.append((newR-1,newY))
                        stack.append((newR,newY+1))
                        stack.append((newR,newY-1))
        return islands

# binary tree bfs


# binary tree dfs



# topological sort
# https://leetcode.com/problems/minimum-height-trees/ not basic, so don't include full code





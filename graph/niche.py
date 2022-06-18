### topological sort
# topological sort
    # topological sorting is only for Directed Acylic Graph (directed and no cycle)
    # topological print nodes that come first, the first vertex is always a vertex with no incoming edges
    # purpose -> schedule system where first task comes before second task
    # how -> temporary stack, a vertex is pushed into the stack when all of its adjacent vertices (and their adjacent vertices and so on) are already in the stack
# https://leetcode.com/problems/minimum-height-trees/ topological. very short buildGraph
    # centroids of the circle, i.e. nodes that is close to all the peripheral nodes (leaf nodes).
    # step base cases input only 2 nodes 
    # step 1 -> get all leaves
    # step 2 -> queue until only 2 nodes left. remove leaf from adjancency list (bi-directional). add new leaf.
    # 



### Dijkstra 

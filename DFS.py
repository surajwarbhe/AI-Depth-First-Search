# DSF ASSIGNMENT
# Create a graph
Graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'G': ['E', 'H'],
    'E': ['B', 'F'],
    'F': ['A'],
    'D': ['F'],
    'H': ['A'],
}

# function of DFS
def DFS(Graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in Graph[node]:
            DFS(Graph, n, visited)
    return visited


start = input("Enter starting vertex : ")
print("The Depth-First Search of the following Graph: ") 

visited = DFS(Graph, start, [])
for i in visited:
    print(i, end=' ')

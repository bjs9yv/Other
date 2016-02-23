# bare bones Depth First Search 
def dfs(graph, start):
    stack = [start]
    visited = set()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# returns all paths from start to goal 
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# more efficient to move this into dfs_paths
def pick_least_path(paths):
    least = paths[0]
    for path in paths:
        if len(path) < len(least):
            least = path
    return least

if __name__ == "__main__":
    graph = {'A': set(['B','E',]),
         'B': set(['A','C', 'F']),
         'C': set(['B','G']),
         'D': set(['H','L']),
         'E': set(['A','I', 'F']),
         'F': set(['E','J', 'K']),
         'G': set(['C','K']),
         'H': set(['D','L']),
         'I': set(['E','J']),
         'J': set(['F','I']),
         'K': set(['G','F'])}
    paths = list(dfs_paths(graph,'A', 'G'))
    print('all paths: ', paths)
    least_path = pick_least_path(paths)
    print('least path: ', least_path)

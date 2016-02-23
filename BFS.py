# bare bones Breadth First Search
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# returns all paths from start to goal
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# more efficient to more this into bfs_paths
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
    paths = list(bfs_paths(graph,'A','G'))
    print('all paths: ', paths)
    least_path = pick_least_path(paths)
    print('least path: ', least_path)

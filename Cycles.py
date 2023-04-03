def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))
            
 def dir_cyclic(graph):
    #Return True if the directed graph has a cycle.
    #graph is a dictionary mapping vertices to each other

    #cyclic({1: (2,), 2: (3,), 3: (1,)})
    #cyclic({1: (2,), 2: (3,), 3: (4,)})
    path = set()
    visited = set()

    visited = set()
    path = [object()]
    path_set = set(path)
    stack = [iter(graph)]
    while stack:
        for v in stack[-1]:
            if v in path_set:
                return True
            elif v not in visited:
                visited.add(v)
                path.append(v)
                path_set.add(v)
                stack.append(iter(graph.get(v, ())))
                break
        else:
            path_set.remove(path.pop())
            stack.pop()
    return False

#Find a path between two vertices
def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
 
#Find all paths between two vetices 
def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

#Find the shortest path between two vertices
def find_shortest_path(graph, start, end):
        dist = {start: [start]}
        q = deque(start)
        while len(q):
            elem = q.popleft()
            for next in graph[elem]:
                if next not in dist:
                    dist[next] = [dist[elem], next]
                    q.append(next)
        return dist.get(end)
        
        

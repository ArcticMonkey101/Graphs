#DFS - Depth First Search
def dfs(al,visited,v):  # al is adjacency list; visited is list (True if v is visited); v is vertex, start from v
      visited[v] = True
      for u in al[v]:
        if not visited[u]:
          dfs(al, visited, u)
      return visited
      
      
#BFS - Breadth First Search

from queue import Queue   # put = push; get = pop

def bfs(al, start, end):
        n = len(al)
        visited = [False for _ in range(n)]
        q = Queue()
        q.put(start)

        while not q.empty():
          u = q.get()
          visited[u] = True

          for w in al[u]:
            if not visited[w]:
              visited[w] = True
              q.put(w)

        return visited[end]

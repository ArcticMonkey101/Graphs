# Create an Adjacency List  
def create_al ():
        l = []
        n = int(input('Enter the total number of elements : '))
        for i in range(n):
            l_temp = []
            for j in range(n):
              val = input('1/0 ? ')
              if val == 1:
                l_temp.append(j)
            l.append(l_temp)
        return l

# Create an adjacency matrix
def adj_mat(al):      #al is the adjacency list
        n = len(al)
        A = [ [0 for _ in range(n)] for _ in range(n)]
        for v in range(n): # for each vertex
          for u in al[v]:  # go over neighbors
            A[u][v] = 1
        return A

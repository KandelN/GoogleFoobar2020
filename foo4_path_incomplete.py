#FOOBar challange problem
#Incomplete solution

import termcolor

class Matrix():
    def __init__(self, arr):
        self.mat = arr
        self.order = len(self.mat)

    def improve(self, n):
        for i in range(self.order):
            for j in range(self.order):
                if i == j or i == n or j == n:
                    continue
                self.mat[i][j] = min(self.get_cost(i,j) , self.get_cost(i,n) + self.get_cost(n, j))
                

    def improve_all(self):    
        for i in range(len(self.order)):
            A.improve(i)

    def get_cost(self, i, j):
        return self.mat[i][j]

    def __repr__(self):
        print("\n")
        for i in self.mat:
            for j in i:
                termcolor.cprint(j, "green", end='\t')
            print('\n\n')
        return("\n")


class Node():
    def __init__(self, state, bunny):
        self.state = state
        self.bunny = bunny
        
class Frontier():
    def __init__(self):
        self.frontier = []

    def empty(self):
        return len(self.frontier) == 0
    
    def add(self, node):
        self.frontier.append(node)
    
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node

A = Matrix([
    [0,2,2,2,-1],   #0
    [9,0,2,2,-1],   #1
    [9,3,0,2,-1],   #2
    [9,3,2,0,-1],   #3
    [9,3,2,2, 0]    #4
])

def main():
    #initialize everything:
    start = Node(0, 0) 
    frontier = Frontier()
    frontier.add(start)
    explored = set()
    while True:
        
        #empty frontier test:
        if frontier.empty():
            raise Exception("No Solution")

        #remove a node form frontier
        node = frontier.remove()
        
        #goal test 
        if node.state == 4:
            return node.bunny
        
        #update explored
        explored.add(node)

        #update frontier
        print("ORD",A.order)
        for x in range(1, A.order-1):
            new = Node(x, node.bunny + 1)
            frontier.add(new)





print("A:", A)
#A.improve(4)
#print("A4:", A)

for i in range(5):
    A.improve(i)
    print(f"A{i}:", A)

print(main())

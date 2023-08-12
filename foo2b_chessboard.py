class Node():
    def __init__(self, pos, counter):
        self.pos = pos
        self.counter = counter


class Frontier():
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)

    def contains_pos(self, pos):
        return any(node.pos == pos for node in self.frontier)
        
    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        #assuming frontier is not empty
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node


def neighbors(pos):
    neigh = []
    for i in ["l","r"]:
        for j in ["b","t"]:
            for x, y, z in [(j, i, i), (j, j, i)]:
                new = move(pos, x)
                if new is not None:
                    new = move(new, y)
                    if new is not None:
                        new = move(new,z)
                        if new is not None:
                            neigh.append(new)  
    return neigh
        

def move(pos, n):
    top_wall = [x for x in range(0, 8)]
    bottom_wall = [x+56 for x in top_wall]
    left_wall = [8*x for x in top_wall]
    right_wall= [x+7 for x in left_wall]
    walls = {
        "t" : top_wall,
        "l" : left_wall,
        "r" : right_wall,
        "b" : bottom_wall
    }
    action = {
        "t" : -8,
        "b" : 8,
        "l" : -1,
        "r" : 1
    }    
    if pos not in walls[n]:
        new = pos + action[n]
        return new
    
    return None
    

def solution(src, target):

    explored = set()
    start = Node(src, 0)
    frontier = Frontier()
    frontier.add(start)

    while True:
        #No solution condition:
        if frontier.empty():
            return None
        #remove
        node = frontier.remove()
        #goal test
        if node.pos == target:
            return node.counter
        #add to explored set
        explored.add(node.pos)
        #expand neighbors
        for position in neighbors(node.pos):
            if position not in explored and not frontier.contains_pos(position):
                new = Node(position, node.counter + 1)
                frontier.add(new)
    


#print("\nMinimum Number of moves required: ",solution(int(input("Source: ")), int(input("Target: ")) ))

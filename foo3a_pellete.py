class Node():
    def __init__(self, num, counter):
        self.num = num
        self.counter = counter


class Frontier():
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)

    def contains_num(self, num):
        return any(node.num == num for node in self.frontier)
        
    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node


def neighbors(num):
    if num%2 == 0:
        return [num/2]
    else:
        return [num -1 , num +1]

def solution(strn):
    number = int(strn)
    #initialize 
    start = Node(number, 0)
    frontier = Frontier()
    frontier.add(start)
    explored = set()

    while True:
        #no solution test
        if frontier.empty():
            return None
        #remove node
        node = frontier.remove()
        #goal test 
        if node.num == 1:
            return node.counter
        #add to explored set
        explored.add(node.num)
        #expand neighbors
        for n in neighbors(node.num):
            if n not in explored and not frontier.contains_num(n):
                new = Node(n, node.counter + 1)
                frontier.add(new)


print(solution(input("ENTER A NUMBER: ")))

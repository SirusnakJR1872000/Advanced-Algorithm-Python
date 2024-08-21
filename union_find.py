# now lets understand the concept of union find
# where we keep a track of nodes connected in a graph and detect the cycles in a graph

# lets start by defining a class where we would all the operations

class UnionFind:
    # define a constructor for initializing the parent and the rank hashmaps
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        # now we iterate through the loop
        for i in range(1, n + 1):
            # initializing the parent at the initial position and rank at 0
            self.par[i] = i
            self.rank[i] = 0

    # now lets write a function to find an element 
    def find(self, n):
        # now lets start with the parent at node n
        p = self.par[n]
        # if the node is not a parent or a root node
        while p != self.par[p]:
            # we perform path compression
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    

    # now lets see how we can find the union by height / rank
    def union(self, n1, n2):
        # we will initalize 2 variable to store root/parent of n1 and n2
        p1, p2 = self.find(n1), self.find(n2)
        # now we need to check if the parents are in the same union
        if p1 == p2:
            return False
        
        # now for union by rank/height there would be 3 conditions:
        # if p1 is taller
        if self.rank[p1] > self.rank[p2]:
            # then we attach p2 to p1
            self.par[p2] = p1
        # if p2 is taller
        elif self.rank[p2] > self.rank[p1]:
            # then we attach p1 to p2
            self.par[p1] = p2
        # now if both the parents have same rank
        else:
            # then we can just choose one parent and attach it to another 
            self.par[p1] = p2
            # and then increase the rank of that node 
            self.rank[p2] += 1
        return True

# lets try to understand the concept of Segment Trees
# Segment Trees are considered to be one of the most complex tree structures

# first lets start with defining the class
class SegmentTree:
    # define a constructor function that takes in the total and left and right pointers
    def __init__(self, total, L, R):
        self.sum = total
        # we will first set the left and right child of current node to None
        self.left = None
        self.right = None
        # defining the left pointer
        self.L = L
        # defining the right pointer
        self.R = R

    # now lets define a static method for building the segment tree
    @staticmethod
    def build(nums, L, R):
        # if it is a single element/ leaf 
        if (L == R):
            return SegmentTree(nums[L], L, R)
        
        # if not then we calculate the mid value
        M = (L + R) // 2
        # we create a root segment which would have the initial total as 0 with left and right pointers
        root = SegmentTree(0, L, R)
        # then we traverse the left subtree
        root.left = SegmentTree.build(nums, L, M)
        # and the right subtree
        root.right = SegmentTree.build(nums, M + 1, R)
        # now we just calculate the sum of the left and right subtree
        root.sum = root.left.sum + root.right.sum
        # and return the value of root
        return root 


    # now lets see how we can update the value in the segement tree in O(log n)
    def update(self, index, val):
        # we will check if the node is a leaf node
        if self.L == self.R:
            # then we just update the value
            self.sum = val
            return
        
        # if it is not a leaf node then we first calculate the mid value to traversw down
        M = (self.L + self.R) // 2
        # if the index to be updated is greater than mid then we recursively call the update function   
        if index > M:
            self.right.update(index, val)
        # if the index is smaller then we recursively call the update on left side
        else:
            self.left.update(index, val)
        # now we calculate the sum of the left and the right child
        self.sum = self.left.sum + self.right.sum   


    def QueryRange(self, L, R):

        # if the query range matches the current node then we return the sum
        if L == self.L and R == self.R:
            return self.sum
        # now lets calculate the mid value
        M = (self.L + self.R) // 2
        # if the left bound is greater than mid then the range lies on right side
        if L > M:
            return self.right.rangeQuery(L, R)
        # if the right bound is less than or equal to mid then the range lies on left side
        elif R <= M:
            return self.left.rangeQuery(L, R)
        # if neither of the conditons are satisfied then we split the query in 2 parts: 
        # right and left
        # and return the sum of those parts
        else:
            return (self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R))

    
        
    
    
        
        



    


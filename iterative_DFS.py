# lets take a look into a iterative approach of the DFS

# now lets start with defining the treeNode which takes in the values at node, left and right child
class treeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# lets start with the inorder traversal
def inorder(root):
    # lets initialize a stack to keep track of nodes
    stack = []
    # initislly we set the current node to the root
    curr = root

    # now we will iterate till our curr and stack are not NULL
    while curr or stack:
        # if our curr is not None
        if curr:
            # then we just push the node into the stack
            stack.append(curr)
            # and move our current pointer to the leftmost node
            curr = curr.left
        # if somehow our current pointer goes to None
        else:
            # then we remove the most recent node
            curr = stack.pop()
            # and we print the value 
            print(curr.val)
            # then we just move to the right child
            curr = curr.right

# lets see the preorder traversal
def preorder(root):
    # now initialize the stack to keep track of node
    stack = []
    # and the current pointer to the root
    curr = root

    # now if the current pointer and stack are not None
    while curr or stack:
        # if current value is not None
        if curr:
            # then we print the current value 
            print(curr.val)
            # now we check if thee exists a right child
            if curr.right:
                # if there is then we just append it to the stack because we want to visit it later
                stack.append(curr.right)
            # now we continue the left side traversal
            curr = curr.left
        # if the current and stack is not None
        else:
            # then we just pop the value because we have reached the end of the tree
            curr = stack.pop()

# now lets see the post order traversal
def postorder(root):
    # stack will hold the node that is to be processed
    stack = [root]
    # another stack which checks if the node is visited or not
    visit = [False]

    # now we traverse till the stack is not empty
    while stack:
        # the top node and the corresponding visited status are popped out
        curr, visited = stack.pop(), visit.pop()
        # if the current is not None
        if curr:
            # we will check if the node has been visited before
            if visited:
                # if it is already visited then we print true
                print(curr.val)
            else:
                # we push the current node back into the stack with 
                # a marker indicating that it has been visited
                stack.append(curr)
                visit.append(True)

                # add the right child to the stack
                stack.append(curr.right)
                visit.append(False)

                # add the left child to the stack
                stack.append(curr.left)
                visit.append(False)
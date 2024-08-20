# lets understand the slow and fast pointers
# they are very much similar to the doubly linked list where we have a next and previous pointer

# first lets try to find the middle of the list with the help of slow and fast pointers

# lets start with defining a method which takes in head which is the start of the list
def middleOfList(head):
    # now we initialize both pointers at the head of the list
    slow, fast = head, head
    # now we run the loop till the fast and the node next to fast is not null
    while fast and fast.next:
        # we will increment slow once
        slow = slow.next
        # and fast pointer twice
        fast = fast.next.next
    # since we are incrementing fast 2 times then it is quite obvious that 
    # the middle has to be at the location of slow pointer 
    return slow

# now lets see how we can check if the list has a cycle or not
# the main idea here is that if the slow and the fast pointer
# converge at a single node then and only then we can say that
# there is a cycle in the list
def hasCycle(head):
    # again we will initialize both the pointers to the head
    slow, fast = head, head
    # we will iterate till the fast and the node next to fast is not null
    while fast and fast.next:
        # we increment the slow pointer
        slow = slow.next
        # and the fast pointer
        fast = fast.next.next
        # if both the pointers converge
        # that means there is a cycle
        if slow == fast:
            return True
    # else we return false
    return False

# now lets see how we can find the head of the cycle
# the given pointers i.e. slow and fast can help us determining
# whether the given list has a cycle or not
# but for finding out the head we need another pointer
def checkHead(head):
    # we will initialize th slow and fast pointers to head
    slow, fast = head, head
    # and iterate till fast and the node next to fast is not null
    while fast and fast.next:
        # now we increment the slow pointer
        slow = slow.next
        # and then the fast pointer
        fast = fast.next
        # if both the pointer converge then a cycle is detected hence we break to find the head
        if slow == fast:
            break
    
    # the fast or the node next to fast does not exist then we can just return None
    if not fast or not fast.next:
        return None

    # lets define another pointer at head after both the pointers converge    
    slow2 = head
    # now to find the head of cycle both the slow pointers should converge
    while slow != slow2:
        # hence we keep on incrementing both the slow pointers
        slow = slow.next
        slow2 = slow2.next
    # nad finally we cn return the value at slow
    return slow
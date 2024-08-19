# lets understand the slinding window algorithm where window is of fixed length

# let us consider a simple example where we are given an array and
# we have to return true if there are 2 elements within a window of size k
# that are equal

# Approach - 1: Brute Force

# lets first define the function which takes the array and the target variable
def bruteForce(nums, k):
    # now lets iterate through the loop till the length of the array
    for L in range(len(nums)):
        # and right pointer will start from the next of left pointer
        # because the first element is going to be the same if L and R are on same location
        # we will go till the minimum of next position to L and L + k
        for R in range(L + 1, min(len(nums), (L + k))):
            # now we compare the value 
            if nums[L] == nums[R]:
                # if they are same we return True
                return True
    # otherwise we return False
    return False

# now lets try to solve the problem using sliding window of fixed size
# in O(n) times

# we define a fucntion which takes in the array and the window size
def slidingWindow(nums, k):
    # now we define a hash set
    window = set()
    # and left pointer to 0
    L = 0

    # now we iterate the right pointer till the length of the array
    for R in range(len(nums)):
        # now we check the size of window if it is greater than the defined one
        if R - L + 1 > k:
            # if it is greater then we remove the left most element from the window
            window.remove(nums[L])
            # and increment the left pointer
            L += 1
        # now we check if the element at R is in the hash or not
        if nums[R] in window:
            # if it is already in hash we return true value
            return True
        # otherwise we add it to the hash set
        window.add(nums[R])

    return False


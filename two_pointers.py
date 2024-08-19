# lets understand the two pointers concept
# so lets check if the given string is a palindrome or not

# lets define a function which takes in string/ number
def isPalindrome(word):
    # now define a left and a right pointer
    L, R = 0, len(word) - 1
    # now we will continue to loop through the word till 
    # left pointer and right pointer didn't cross each other
    while L < R:
        # if the element at left pointer and right pointer doesn't match 
        # then we straight away terminate the loop
        if word[L] != word[R]:
            return False
        # now we will increment the left pointer to go to the new element
        L += 1
        # and decrement the right pointer
        R -= 1
    
    return True

# now lets consider another example where we are given a sorted array of integers
# we have to return the indices of 2 elements that sum up to the target value. 

# lets start with defining a function with which takes in the array and the target value
def targetSum(nums, target):
    # lets define the left and right pointer
    L, R = 0, len(nums) - 1
    # now we will iterate through the loop till the left and right pointers have not crossed each other
    while L < R:
        # now we will check if the sum of left and right pointer is greater than target
        if nums[L] + nums[R] > target:
            # we will decrement the right pointer because we know that array is sorted
            R -= 1
        # now we check if the sum is less than target value
        elif nums[L] + nums[R] < target:
            # we will increment the left pointer
            L += 1
        # now if it is equal then we return the pointers
        else:
            return [L, R]

            
        

    
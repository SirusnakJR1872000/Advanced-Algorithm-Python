# now lets understand sliding window algorithm where the window is of variable size

# lets consider an example in this case :
# we have to find the length of longest subarray with the same value in each position
# that is we need to make sure that we do not have any holes in the subarray or the window

# we define a function which takes an array as the input
def longestSubarray(nums):
    # initially we set the length of subarray to 0
    length = 0
    # and left pointer to 0
    L = 0

    # now we iterate through the loop till the length of the array
    for R in range(len(nums)):
        # if the immediate element is not the same as previous element
        if nums[L] != nums[R]:
            # then we bring L and R pointer at the same location
            L = R
        # now we calculate the length of current subarray/window
        length = max(length, R - L + 1)
    # now we can return the length after we exit the loop
    return length

# now lets consider another example where we want to find the length of 
# minimum subarray where the sum is greater than or equal to the target
# assume all values are psoitive

# lets define a function which takes in array and the target value
def shortestSubarray(nums, target):
    # we set the total and left pointer to 0
    L, total = 0, 0
    # we set the length to maximum value possible hence infinity
    length = float("inf")

    # now we will iterate through the array
    for R in range(len(nums)):
        # now we will add the elements to the total
        total += nums[R]
        # if the total is greater than or equal to the target(as per our condition)
        #  then we have to compute the length
        while total >= target:
            # we find the minimum of the lengths
            length = min(R - L + 1, length)
            # since we will be shifting the window we will subtract the value of the 
            # element at the left position
            total -= nums[L]
            # and increment the left pointer
            L += 1
    # now if our length is equal to initial value of infinity 
    # which means we didn't find any subarray to satisfy our condition
    return 0 if length == float("inf") else length




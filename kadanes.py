# lets understand the Kadane's algorithm where we calculate the maximum sum subarray ending at a particular position
# first lets try with the brute force approach

# the algorithm takes in the array nums
def bruteForce(nums):
    # and we take the max number to the first index
    maxSum = nums[0]

    # now we iterate through the length of the array
    for i in range(len(nums)):
        # we set the current sum to zero
        currSum = 0
        # now we have to iterate through the first pointer to the length of array
        for j in range(i, len(nums)):
            # now we add the currSum with the element at which j is pointing
            currSum += nums[j]
            # now we store the maximum value at maxSum by using max()
            maxSum = max(maxSum, currSum)
    return maxSum

# now lets optimize the Kadane's algorithm
# here the pattern is that if we have a negative subarray we should discard and start a new subarray
# because the negative number only makes the sum smaller

# we take the array as input
def Kadanes(nums):
    # we set the current max value to the first value of array
    maxSum = nums[0]
    # and current Sum to 0
    currSum = 0

    # now we iterate till the numbers in array
    for n in nums:
        # now we set the value of currSum as the maximum of 0 and current value of the sum
        # because we don't want to take negative value
        currSum = max(currSum, 0)
        # now we just add the next element to the current value
        currSum += n
        # and finally we check for the maximum between the maxSum which we initialized earlier and current value of sum
        maxSum = max(maxSum, currSum)
    # and return the value of maximum of the sum
    return maxSum

# now imagine we want to know the starting and ending index of the subarray through which we calculate the maximum sum
# we use an algorithm called sliding window
# it is just another variation of Kadanes algorithm

# we define a function which takes an array
def slidingWindow(nums):
    # we set the maximum value of subarray to the first element 
    maxSum = nums[0]
    # and current sum to 0
    currSum = 0
    # now we define 2 variable to keep track of the max values
    maxL, maxR = 0, 0
    # define a left pointer to 0
    L = 0

    # now we will iterate the right pointer till the length of array
    for R in range(len(nums)):
        # now we want to check if the currSum is less than 0 that is if it is negative
        if currSum < 0:
            # if it is negative we just set it to zero
            currSum = 0
            # and keep both the pointers at same location
            L = R

        # now we just calculate the value of current sum by adding with the next element
        currSum += nums[R]
        # now we see if the current pointer is current sum is greater than maximum Sum
        if currSum > maxSum:
            # if the condition is satisfied then we assign the value fo current sum to max sum
            maxSum = currSum
            # and we assign the value of left and right pointer to maxL and maxR
            maxL, maxR = L, R
    
    return [maxL, maxR]


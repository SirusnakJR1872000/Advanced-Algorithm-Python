# so lets understand the concept of prefix sum
# as the word suggest prefix means at the start
# we pick the starting element and continue the operation

# so lets assume that we have an array of values and we need to 
# design a system that can query the sum of subarray of values

# lets define a class 
class PrefixSum:
    # a constructor function that takes in the array
    def __int__(self, nums):
        # define an empty array to store the prefix
        self.prefix = []
        # a variable to store the computed value of total
        total = 0

        # now we keep on iterating till all the values in the array
        for n in nums:
            # we add each value to the total 
            total += n
            # and as we calculate we store it in the new array 
            self.prefix.append(total)

    # now we define a function which takes in the 2 pointers
    def rangeSum(self, left, right):
        # cumulative sum of elements from the start to right
        preRight = self.prefix[right]
        # if left > 0 then the sum of elements before index left is stored 
        # else if there are no elements then sum is 0
        preLeft = self.prefix[left - 1] if left > 0 else 0
        # the sum of elements in the range of right to left
        return (preRight - preLeft)
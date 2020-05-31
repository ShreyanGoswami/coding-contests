# Given the array of integers nums, you will choose two different indices i and j of that array. 
# Return the maximum value of (nums[i]-1)*(nums[j]-1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = 0
        nums.sort()
        val1 = nums[-1]
        val2 = nums[-2]
        return (val1-1)*(val2-1)
        
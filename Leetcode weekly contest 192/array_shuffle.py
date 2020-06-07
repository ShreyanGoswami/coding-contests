'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''
        frm = n
        to = 1
        while frm < 2 * n:
            nums.insert(to, nums.pop(frm))
            frm += 1
            to += 2
        return nums
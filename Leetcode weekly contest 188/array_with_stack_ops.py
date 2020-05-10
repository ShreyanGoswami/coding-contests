'''
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.
'''
from typing import List

def buildArray(self, target: List[int], n: int) -> List[str]:
        '''
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        res = []
        s = set(target)
        prefixSum = [0, 1]
        for i in range(2, n+1):
            if i in s:
                prefixSum.append(prefixSum[i-1] + i)
            else:
                prefixSum.append(prefixSum[i-1])
        for i in range(1, n+1):
            if i in s:
                res.append('Push')
            else:
                if prefixSum[n] - prefixSum[i] == 0:
                    break
                res.append('Push')
                res.append('Pop')
        return res


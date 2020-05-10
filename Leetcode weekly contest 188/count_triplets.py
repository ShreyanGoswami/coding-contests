'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.
'''
from typing import List

def countTriplets(self, arr: List[int]) -> int:
        prefixSum = []
        n = len(arr)
        count = 0
        for i in range(0, n):
            prefixSum.append([0] * n)
        
        
        for i in range(0, n):
            for j in range(0,i-1):
                prefixSum[i][j] = 0
            prefixSum[i][i] = arr[i]
            for j in range(i+1, n):
                prefixSum[i][j] = prefixSum[i][j-1] ^ arr[j]
                 
        for i in range(0, n-1):
            for j in range(i+1, n):
                for k in range(j, n):
                    if prefixSum[i][j-1] == prefixSum[j][k]:
                        count += 1
        return count
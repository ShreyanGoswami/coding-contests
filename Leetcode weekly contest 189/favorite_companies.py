'''
Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).
Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. 
You must return the indices in increasing order.
'''
from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        for i in range(len(favoriteCompanies)):
            favoriteCompanies[i] = set(favoriteCompanies[i])
        res = []
        for i in range(len(favoriteCompanies)):
            setA = favoriteCompanies[i]
            isSubset = False

            for j in range(len(favoriteCompanies)):
                if j != i:
                    setB = favoriteCompanies[j]
                    if setA.issubset(setB):
                        isSubset = True
                        break
            if isSubset == False:
                res.append(i)
        return res
        
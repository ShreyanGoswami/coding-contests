'''
Given two integer arrays startTime and endTime and given an integer queryTime.
The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
Return the number of students doing their homework at time queryTime. 
More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
'''
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''
        n = len(startTime)
        total = 0
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                total += 1
        return total
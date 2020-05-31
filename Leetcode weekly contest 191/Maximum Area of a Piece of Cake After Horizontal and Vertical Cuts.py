# Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts 
# where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position 
# provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.

from typing import List
class Solution:
    def maxArea(self, h: int, w: int, hcuts: List[int], vcuts: List[int]) -> int:
        '''
        Time complexity O(nlogn)
        Space complexity O(n)
        '''
        hcuts.append(0)
        hcuts.append(h)
        hcuts.sort()
        vcuts.append(0)
        vcuts.append(w)
        vcuts.sort()

        hcutsdiff = [0] * len(hcuts)
        hcutsdiff[0] = 0
        for i in range(1, len(hcuts)):
            hcutsdiff[i] = hcuts[i] - hcuts[i-1]
        
        vcutsdiff = [0] * len(vcuts)
        vcutsdiff[0] = 0
        for i in range(1, len(vcuts)):
            vcutsdiff[i] = vcuts[i] - vcuts[i-1]
        
        maxH1 = max(hcutsdiff)
        maxV1 = max(vcutsdiff)
        return ((maxH1)*(maxV1)) % (10**9+7)

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea(5,4,[3,1],[1]))
    print(s.maxArea(5,4,[3],[3]))
    print(s.maxArea(5,4,[2,1,4],[1,3]))
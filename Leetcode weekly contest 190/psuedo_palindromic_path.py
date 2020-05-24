'''
Given a binary tree where node values are digits from 1 to 9. 
A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isPsuedoPalindrome(self, l):
        from collections import Counter
        d = Counter(l)
        isOddPresent = False
        for k, v in d.items():
            if v % 2 != 0:
                if isOddPresent == True:
                    return False
                else: isOddPresent = True
        return True
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        l = []
        count = [0]
        def traverse(curr, path, count):
            if curr is None:
                return
            if curr.left is None and curr.right is None:
                path.append(curr.val)
                if self.isPsuedoPalindrome(path):
                    count[0] += 1
                path.pop()
            else:
                path.append(curr.val)
                traverse(curr.left, path, count)
                traverse(curr.right, path, count)
                path.pop()
        traverse(root,l,count)
        return count[0]
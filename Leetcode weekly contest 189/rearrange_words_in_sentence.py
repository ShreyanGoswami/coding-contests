'''
Given a sentence text (A sentence is a string of space-separated words) in the following format:

First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.
'''

class Solution:
    def arrangeWords(self, text: str) -> str:
        '''
        Time complexity: O(nlogn)
        Space complexity: O(n*m) where n is the number of words and m is the maximum number of letters in a word
        '''
        words = text.split()
        words[0] = words[0].lower()
        words.sort(key = lambda x: len(x))
        words[0] = words[0].capitalize()
        return " ".join(x for x in words)
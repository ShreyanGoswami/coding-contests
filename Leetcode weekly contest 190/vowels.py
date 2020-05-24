'''
Given a string s and an integer k.
Return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are (a, e, i, o, u).
'''
class Solution:
    
    def countVowels(self, d):
        vowels ={'a','e','i','o','u'}
        count = 0
        for k,v in d.items():
            if k in vowels:
                count += v
        return count
    
    def maxVowels(self, s: str, k: int) -> int:
        from collections import Counter
        
        start = 0
        end = k-1
        d = Counter(s[start:end+1])
        maxcount = 0
        while True:
            count = self.countVowels(d)
            if count >= k:
                return k
            elif count > maxcount:
                maxcount = count
            if end == len(s):
                break
            d[s[start]] -= 1
            start += 1
            end += 1
            try:
                d[s[end]]+=1
            except KeyError:
                d[s[end]]=1
            except IndexError:
                pass
        return maxcount

if __name__ == "__main__":
    s = Solution()
    s.maxVowels('weallloveyou', 7)
        
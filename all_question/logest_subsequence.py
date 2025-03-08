class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = -float('inf')
        for i in range(len(s)):
            temp = set()
            for j in range(i , len(s)):
                if s[j]  in temp:
                    break
                temp.add(s[j])
                max_len = max(max_len , j - i  + 1)
                
        return max_len
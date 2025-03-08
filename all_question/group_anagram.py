class Solution:
    def group_Anagram(self,strings :list):
        count = {}
        
        for i in strings:
            sorted_str = ''.join(sorted(i))
            if sorted_str not in count:
                count[sorted_str] = [i]
            else:
                count[sorted_str].append(i)
                

        ans = list(count.values())

        return ans
    
strings = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
ans  = sol.group_Anagram(strings)

print(ans)        
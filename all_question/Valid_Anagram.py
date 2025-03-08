class Solution:
    def Valid_anagram(self , str1 , str2):
        dict = {}
        
        for i in str1:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                
            
        for i in str2:
            if i not in  dict :return False
            elif dict[i] == 1: del dict[i]
            else:
                dict[i] -= 1
                
        return not dict
    
    def valid_anagram_2(self , str1 , str2):
        temp = [0] *  26
        for i in str1:
            temp[ord(i.lower()) - ord('a')]  += 1
        
        for i in str2:
            # if temp[ord(i.lower()) - ord('a')] == 0: 
            #     return False
            # elif  temp[ord(i.lower()) - ord('a')] == 1:
            temp[ord(i.lower()) - ord('a')] -= 1
            # else:
            #      temp[ord(i.lower()) - ord('a')] -= 1
                 
        # for i in temp:
        #     if i > 0:
        #         return False 
            
        return all(x == 0 for x in temp)
    
sol = Solution()
# s = "anagram"
# t = "nagaram"

s = 'rat'
t = 'cat'

print(sol.valid_anagram_2(s,t))
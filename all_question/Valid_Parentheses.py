class Solution:
    def isValid(self ,s:str)-> bool:
        stack = []
        match_dict = {')' :'(',
                      '}' :'{',
                      ']' :'['
                      }
        for i in s:
            if i in match_dict.values():
                stack.append(i)
                
            elif i in match_dict.keys():
                if not stack or stack.pop() != match_dict[i]:
                    return False
            
        return not stack
    
    
s = '(((])))'
sol = Solution()
if sol.isValid(s):
    print('valid parentheses')
else:
    print('not valid parentheses')
        
        
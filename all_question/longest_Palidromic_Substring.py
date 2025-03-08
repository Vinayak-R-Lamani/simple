# def is_palidrome(s: str):
#     i  , j = 0 , len(s) - 1
#     while i  < j:
#         if s[i] != s[j]:
#             return False
#         i +=1
#         j -=1
#     return True


# max_len = 0

# for i in range(len(s)):
#     for j in range(i , len(s)):
#         if is_palidrome(s[i:j + 1]):
#             max_len = max(max_len , j - i + 1)
        
# print(max_len)

def longest_Palindromic(s:str):
    res = ""
    res_len = 0
    for i in range(len(s)):
        # odd length
        l , r = i , i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res = s[l : r +1]
                res_len = r -l + 1
                
            l -= 1
            r += 1
        
        # even length
        l , r = i , i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res = s[l : r +1]
                res_len = r -l + 1
                
            l -= 1
            r += 1
            
    return res
s = "babad"
ans = longest_Palindromic(s)
print(ans)
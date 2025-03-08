s = "AABABBA"
k = 1

# max_len = 0
# for i in range(len(s)):
#     hash_array = [0] * 26
#     max_j = 0
#     changes = 0
#     for j in range(i , len(s)):
#         hash_array[ord(s[j]) - ord('A')] +=1
#         max_j = max(max_j ,hash_array[ord(s[j]) - ord('A')] )
#         changes = (j - i + 1) - max_j
#         if changes <=  k:
#             max_len = max(max_len , j - i + 1)
#         else:
#             break
        
        
# print(max_len)


def characterReplacement(s : str , k :int) -> int:
    count = {}
    left = 0
    max_freq = 0
    max_length = 0
    
    for right in range(len(s)):
        count[s[right]] = count.get(s[right] ,0) + 1
        max_freq = max(max_freq , count[s[right]])
        
        if (right - left + 1) - max_freq > k:
            count[s[left] ] -=1
            left += 1
            
        max_length = max(max_length , right - left + 1)
        
    return max_length
s = "AABABBA"
k = 1

ans = characterReplacement(s , k)
print(ans)
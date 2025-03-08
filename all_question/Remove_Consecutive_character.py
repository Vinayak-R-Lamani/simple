def remove_consecutive_characters(a:str):
    ans = ""
    ans = ans +a[0]
    i = 1
    while i  < len(a):
        if a[i - 1] != a[i]:
            ans = ans + a[i]
        i += 1
            
    return ans

s = 'aabbcccddd'
print(remove_consecutive_characters(s))
            
            
        
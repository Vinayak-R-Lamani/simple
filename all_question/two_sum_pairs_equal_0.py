arr = [-1, 0, 1, 2, -1, -4]

ans = set()
seen = set()

for num in arr:
    if -num in seen:
        ans.add(tuple(sorted([num, -num])))  
    seen.add(num)
    
ans = [list(i) for  i in ans]
print(ans)
fact = 1
for i in range(1, 1001):
    fact *= i
    
ans = [int(i) for i in str(fact)]
print(ans)
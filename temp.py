n = 5
ans = n * n
lst = [int(x)  for x in str(ans)]
ans_ = 0
j = 1
for i in range(0 , len(str(n)) ):
    ans_ += lst[len(lst) - i - 1] * j
    j *= 10
    
print('Automorphic number') if ans_ == n else print('not')

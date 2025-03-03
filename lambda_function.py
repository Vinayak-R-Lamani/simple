# ans = [(lambda i : (i + 10)/2 )(i)for i in range(5)]
ans = list(map(lambda i: (i +10) /2, range(5)))
print(ans)
arr = [3, 30, 34, 5, 9]
# ele = [str(i)  * 10 for i in arr if len(str(i)) <= 10]
# ans = sorted(ele ,key = lambda x : int(x) , reverse = True)
# print(ans)
ele = []

    
arr.sort( key=lambda x :int((str(x) * 10)[:10]) ,reverse=True)
ans = ''.join(map(str , arr))
print("0") if ans[0] == "0" else print(ans)
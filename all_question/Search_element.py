def search_element(arr,element):
    ans = 0
    for i , num in enumerate(arr):
        if num == element:
            ans = i
    print(-1) if ans == 0 else print(ans)
    
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    search_element(arr,6)
            
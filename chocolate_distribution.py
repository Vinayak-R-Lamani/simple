def chocolate_distribution(arr: list , m :int):
    m = m - 1
    arr.sort()
    min_diff = float('inf')
    for i in range(m , len(arr)):
        if arr[i] - arr[i - m] < min_diff:
            min_diff = arr[i] - arr[i - m]
    return min_diff

if __name__ == "__main__":
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    ans = chocolate_distribution(arr,m)
    
    print(ans)
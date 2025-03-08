def longestSubarrayDivK(arr, k):
    n = len(arr)
    res = 0
    prefIdx = {}
    sum = 0

    # Iterate over all ending points
    for i in range(n):
        print(f"before {sum}")
        # prefix sum mod k 
        sum = (sum + arr[i]) % k
        print(f"after {sum}")

        # If sum == 0, then update result with the
        # length of subarray arr[0...i]
        if sum == 0:
            res = i + 1

        # Update max length for repeating sum
        elif sum in prefIdx:
            res = max(res, i - prefIdx[sum])
            print(f"res {res}")

        # Store the first occurrence of sum
        else:
            prefIdx[sum] = i
    print(prefIdx)
    return res

if __name__ == "__main__":
    arr = [2, 7, 6, 1, 4, 5]
    k = 3

    print(longestSubarrayDivK(arr, k))
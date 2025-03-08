def find_repeating(arr: list):
    # sourcery skip: convert-to-enumerate, list-comprehension
    arr.sort()
    temp = []
    i = 0
    for j in range(1, len(arr)):
        if arr[i] == arr[j]:
            temp.append(arr[i])
        i += 1
        
    print(temp)
    
    
if __name__ == "__main__":
    arr = [1,1,2,3,4,4,5,5,2]
    find_repeating(arr)    

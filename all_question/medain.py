def median(arr:list):
    arr.sort()
    n = len(arr)
    if  n % 2 != 0:
        print(arr[n//2])
        
    else:
        print((arr[n //2]+ arr[n//2 -1]) / 2)
        
if __name__ == "__main__":
    arr = [2,2,2,2]
    median(arr) 
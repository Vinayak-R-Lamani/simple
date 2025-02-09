def count_ele(arr: list):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            
    print(dict)
    
if __name__ == "__main__":
    arr = [10,5,10,5,15,10,15]
    count_ele(arr)
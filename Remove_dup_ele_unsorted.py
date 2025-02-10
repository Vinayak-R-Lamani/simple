def remove_ele(arr:list):
    temp = {}
    for i in arr:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] +=1 
            
    print(temp.keys())
    
if __name__ == "__main__":  
    arr = [1,1,2,2,2,3,3]
    remove_ele(arr)
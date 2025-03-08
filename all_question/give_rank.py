def Replace_element(arr:list):
    sorted_arr = sorted(set(arr))
    rank_map = {num:rank + 1 for rank, num in enumerate(sorted_arr)}
    print([rank_map[num] for num in arr])
    
def replace_with_rank(arr:list):
    sorted_arr = sorted(set(arr))
    ranked_arr = []
    
    for num in arr:
        rank = sorted_arr.index(num)+1
        ranked_arr.append(rank)
    print(ranked_arr)
    
if __name__ == "__main__":
    # arr = [20,15,26,2,98,6]
    # arr = [1,2,8,15,8,25,9]
    arr = [40,10,30,20,50]
    replace_with_rank(arr)
        
    
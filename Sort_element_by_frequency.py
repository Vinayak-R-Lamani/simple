from collections import Counter
def sort_element_by_frequency(arr:list):
    fre_cnt = Counter(arr)
    sort_arr = sorted(arr,key = lambda x:(-fre_cnt[x] , arr.index(x)))
    print(sort_arr)

if __name__ == "__main__":
    arr = [1,2,3,2,4,3,1,2]
    sort_element_by_frequency(arr)    
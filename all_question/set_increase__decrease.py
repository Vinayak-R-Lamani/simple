from revese import reverse_array
def set_inc_dic(arr: list):
    arr.sort()
    n = len(arr) // 2
    rev_arr = reverse_array(arr[n:])
    print(arr[:n] + rev_arr)
    

if __name__ == "__main__":
    arr = [1,4,2,6,3,5,7,8]
    set_inc_dic(arr)
    
def Non_repeating_element(string:str):
    dict = {}
    for i in string:
        dict[i] = dict.get(i , 0) + 1
        
    lst = [i for i in string if dict[i] == 1]
    print(lst)
    
if __name__ == "__main__":
    string = 'yahoo'
    Non_repeating_element(string)
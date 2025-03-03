def Calculate_frequency_of_char(string:str):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    sorted_keys =sorted(dict.keys())
    for key in sorted_keys:
        print(f"{key}{dict[key]}",end=" ")
        
if __name__ == "__main__":
    string = "takeuforward"
    # Calculate_frequency_of_char(string)
    dict ={}
    for i in string:
        dict[i] = dict.get(i ,0) + 1
        
    print(dict)
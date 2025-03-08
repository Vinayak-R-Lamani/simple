def Reverse_string(strin:str):
    string = list(strin)
    i  , j = 0 , len(string) - 1
    while i < j:
        string[i] , string [j] =string[j] , string[i]
        i += 1
        j -= 1
        
    print("".join(string))
    
    
if __name__ == "__main__":
    string = "Vinayak"
    Reverse_string(string)
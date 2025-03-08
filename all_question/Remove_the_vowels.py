def Remove_vowels(string:str):
    vowels = "aeiouAEIOU"
    
    for i in string:
        if i in vowels:
            string = string.replace(i, "")
            
    print(string)
    
def Remove_vowels_2(string:str):
    vowels = "aeiouAEIOU"
    for i in vowels:
        string = string.replace(i,"")
    print(string)
    
    
def Remove_vowels_3(string:str):
    vowels = "aeiouAEIOU"
    result = "".join(char for char in string if char not in vowels )
    print(result)
if __name__ == "__main__":
    string = 'take u forward'
    Remove_vowels_3(string)
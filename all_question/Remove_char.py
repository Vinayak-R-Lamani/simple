def Remove_character_from_string(string:str):
    digits = "0123456789"
    result = "".join(char for char in string if char.isalpha())
    print(result)
    
if __name__ == "__main__":
    string =  "1.Python & 2.Java"
    Remove_character_from_string(string)
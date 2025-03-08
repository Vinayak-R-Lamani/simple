def Remove_brackets(string:str):
    brackets = "()"
    print("".join(char for char in string if char not in brackets))
    
if __name__ == "__main__":
    string =  'a+((b-c)+d)'
    Remove_brackets(string)
    
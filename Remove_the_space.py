def Remove_the_space(string:str):
    result = "".join(char for char in string if not char.isspace())
    print(result)
    
if __name__ == "__main__":
    string = 'take u forward'
    Remove_the_space(string)
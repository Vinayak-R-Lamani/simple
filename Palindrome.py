def is_Palindrome(string:str):
    i , j = 0 , len(string) - 1
    while i < j:
        if string[i] != string[j] :
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    string = "ABCDCBA"
    if is_Palindrome(string):
        print("Palindrome")
    else:
        print('Not Palindrome')
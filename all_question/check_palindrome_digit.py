def check_palindrome_digit(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n =  n // 10
    print(True) if original == reverse else print(False)
    
if __name__ == "__main__":
    n = -121
    check_palindrome_digit(n)
        
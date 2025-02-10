def check_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    # return True if original == reverse else False
    return original == reverse

def find_all_palindrome(start, end):
    return [x for x in range(start, end) if check_palindrome(x)]

if __name__ == "__main__":
    ans = find_all_palindrome(100,150)
    print(ans)
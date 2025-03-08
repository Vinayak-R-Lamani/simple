def is_palindrome(num):
    return str(num) == str(num)[::-1]

arr = [121, 131, 20]
def isPalinArray(arr):
    for i in arr:
        if not is_palindrome(i):
            return False
        
    return True


print(isPalinArray(arr))


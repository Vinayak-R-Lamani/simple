def reverse_digit(n):
    ans = ''.join(reversed(str(n)))
    print(int(ans))
    
def reverse_digit_2(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n //10
        
    print(reverse)
    
if __name__ == "__main__":
    n = 154
    reverse_digit_2(n)
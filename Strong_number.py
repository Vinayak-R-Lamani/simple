import math
def get_factorial(n):
    fact = 1
    for i in range(n , 1, -1):
        fact *= i
    return fact

def check__strong_number(n):
    original = n
    summation = 0
    while n > 0:
        digit = n % 10
        summation += get_factorial(digit)
        n //=  10
        
    print(True) if original == summation else print(False)
    
    
def is_strong_number(n):
    return sum(math.factorial(int(num)) for num in str(n)) == n
if __name__ == "__main__":
    n = 40585 
    ans = is_strong_number(n)
    print(ans)
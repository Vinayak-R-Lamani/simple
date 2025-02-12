def prime_number(n):
    if n < 2:
        return False
    for i in range(2 ,( n // 2)+1):
        if n % i == 0:
            return 
        
    return True
def Prime_factor(n):
    return [x for x in range(n) if prime_number(x) and n % x== 0]

if __name__ == "__main__":
    n = 35
    ans = Prime_factor(n)
    print(ans)
    
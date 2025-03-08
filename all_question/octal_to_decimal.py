def octal_to_decimal(n:int):
    decimal = 0
    i = 0
    while n > 0:
        decimal += (n % 10) * (8 ** i)
        i += 1
        n //= 10
        
    print(decimal)
    
    
def octal_to_decimal_2(n:int):
    decimal = 0
    lst = [int(i) for i in str(n)]
    for i , num in enumerate(reversed(lst)):
        decimal += (num * (8 ** i))
    print(decimal)
if __name__ == "__main__":
    n = 170
    octal_to_decimal_2(n)
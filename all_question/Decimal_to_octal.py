def decimal_to_octal(n:int):
    octal_string = ""
    while n > 0:
        octal_string = str(n % 8) + octal_string
        n //= 8
        
    print(octal_string)
    
if __name__ == "__main__":
    n = 393
    decimal_to_octal(n)
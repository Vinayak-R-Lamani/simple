import sys

def replace_0_with_1(n):
    replace = ""
    while n > 0:
        digit = n % 10
        if digit == 0:
            replace = '1'+replace
        else:
            replace = str(digit)+replace
        n //= 10
        
    print(int(replace))
    
def replace_0_with_1_second_method(n):
    result = 0
    place = 1    
    
    if n == 0 :
        print(1)
        return 
    while n > 0:
        digit = n % 10
        if digit == 0:
            digit = 1
        result += digit * place
        place *= 10
        n //= 10
        
    print(result)

if __name__ == "__main__":
    replace_0_with_1_second_method(int(sys.argv[1]))
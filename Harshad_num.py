import sys

def is_Harshad(n):
    original = n
    sum_digits = 0
    while n > 0:
        digits = n % 10
        sum_digits += digits
        n //= 10
        
    if sum_digits == 0:
        print("The number cannot be zero")
    elif original % sum_digits == 0:
        print(f"{original} is harshad number")
    else:
        print(f"{original} is not harshad number")
        
if __name__ == "__main__":
    # is_Harshad(int(''.join(sys.argv[1])))
    if len(sys.argv) != 2:
        print("Usage :python script.py <number>")
    else:
        try:
            number = int(sys.argv[1])
            is_Harshad(number)
            
        except ValueError:
            print("Invalid input. Please provide a valid integer")
    
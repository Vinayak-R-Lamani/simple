import sys

def find_factors(n):
    lst = []
    for i in range(1 , (n//2) + 1):
        if n % i == 0:
            lst.append(i)
            
    return lst

def get_factor(n):
    return [i for i in range(1 , (n //2)+1) if n % i == 0]

def is_Abundant(n):
    if sum(get_factor(n)) < n:
        print('Abundant Number')
        
    else:
        print('not Abundant Number')

if __name__ == "__main__":
    if len(sys.argv ) != 2:
        print("Usage: python script.py <number>")
    else:
        try:
            number = int(sys.argv[1])
            is_Abundant(number)
        except ValueError:
            print('Invalid input')
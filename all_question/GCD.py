import math
def GCD(a ,b):
    gcd  = 1
    for i in range(1 , min(a, b) +1):
        if a % i == 0 and  b % i == 0:
            gcd = i
    print(gcd)
    
def findGCD(a , b):

    for i in range(min(a , b), 0 , -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1
            
    
def Find_GCD(a ,b):
    while a > 0 and b > 0 :
        if a > b:
            a = a % b
        else:
            b = b % a      
    if a == 0:
        return b
    return a

if __name__ == "__main__":
    n1 , n2 = 9999 , 6677
    print(math.gcd(9999,6677))
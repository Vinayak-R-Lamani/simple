import math
def lcm_using_gcd(a,b):
    return abs(a * b) // math.gcd(a ,b)

def lcm_iterative(a ,b):
    max_num = max(a,b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        print(max_num)
        max_num += 1

if __name__ == "__main__":
    a , b = 18 , 36
    print(lcm_iterative(a,b))
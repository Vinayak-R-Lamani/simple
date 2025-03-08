import math

def add_fractions(n1, d1, n2, d2):
    lcm = (d1 * d2) // math.gcd(d1, d2)
    
    numerator = (n1 * (lcm // d1) + n2 * (lcm // d2))
    
    gcd = math.gcd(numerator,lcm)
    numerator //=  gcd
    lcm //= gcd
    
    return f"{numerator}/{lcm}"

if __name__ == "__main__":
    print(add_fractions(3,4,1,7))
    print(add_fractions(5,2,1,2))
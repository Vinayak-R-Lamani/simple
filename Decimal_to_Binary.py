def Decimal_to_binary(n:int) :
    string = ""
    while n > 0:
        string = str(n % 2 ) + string
        n //= 2
        # if n == 1:
        #     string = str(n) + string
            
    print(string)
    
def Alternative_approach(n:int) :
    return bin(n)[2:]

def optimized_approach(n:int):
    if n == 0:
        return "0"
    binary_string = ""
    while n > 0:
        binary_string = str(n & 1 ) + binary_string 
        n >>= 1
        
    print(binary_string)
    
if __name__ == "__main__":
    n = 393
    optimized_approach(n)
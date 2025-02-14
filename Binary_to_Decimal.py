import sys
def binary_to_decimal(n:int) -> int:
    lst = [int(i) for i in str(n)]
    n = len(lst) - 1
    i = 0
    decimal = 0
    for j in range(n , -1, -1):
        if lst[j] == 0:
            i += 1
            continue
        else:
            decimal += (2 ** i)
            i += 1
        
    print(decimal)
    
    
def binary_to_decimal_2(n:int) -> int:
    lst = [int(i) for i in str(n)]
    n = len(lst)
    decimal = 0
    for  i , bit in enumerate(reversed(list)):
        decimal += bit * (2**i)
    print(decimal)
    
if __name__ == "__main__":
    binary_to_decimal_2(int(sys.argv[1]))
def find_maximum_and_minimum(n):
    max_ = max([int(x) for x in str(n)])
    min_ = min([int(x) for x in str(n)])
    print(max_," and ",min_)
    
def find_max_and_min(n):
    min_ = float('inf')
    max_ = float('-inf')
    while n > 0:
        digit = n % 10
        if min_ > digit:
            min_ = digit
        if max_ < digit:
            max_ = digit
        n = n //10
        
    print(max_," and ",min_)
if __name__ == "__main__":
    n = 23004
    find_max_and_min(n)
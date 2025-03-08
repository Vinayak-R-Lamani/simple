def find_factors(n):
    lst = []
    for i in range(1, n +1):
        if n % i == 0:
            lst.append(i)
    print(lst)
    
    
if __name__ == "__main__":
    n = 9
    find_factors(n)
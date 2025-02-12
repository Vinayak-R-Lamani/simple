def factorial(n):
    fact = 1
    for i in range(n , 1  , -1):
        fact *= i
    print(fact)
    
if __name__ == "__main__":
    n = 3
    factorial(n)
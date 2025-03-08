def fibonacci(n):
    t1 = 0
    t2 = 1
    fib = t1 + t2
    print(t1)
    print(t2)
    print(fib)
    for i in range(2 , n):
        t1 = t2
        t2 = fib
        fib = t1 + t2
        print(fib)
        
if __name__ == "__main__":
    n = 6
    fibonacci(n)
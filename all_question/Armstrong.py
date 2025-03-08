def digit_list(n):
    return [int(d) for d in str(n)]

def digit_list_2(n):
    lst = []
    while n > 0:
        digit = n % 10
        lst.append(digit)
        n = n // 10
    return lst

def is_armstrong(digit):
    digits  = digit_list(digit)
    n = len(digits)
    return sum(x ** n for x in digits) == digit

if __name__ == "__main__":
    n = 199
    print(is_armstrong(n))  # True
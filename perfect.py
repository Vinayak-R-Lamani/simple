def is_perfect_number(n):
    return n == sum(x for x in range(1, n) if n % x == 0)

if __name__ == "__main__":
    n = 15
    print(is_perfect_number(n))  # True
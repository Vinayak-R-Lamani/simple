def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def sum_of_natural_numbers_2(n):
    return sum(range(n + 1))

def sum_of_natural_numbers_3(n):
    return sum(x for x in range(n + 1))

if __name__ == "__main__":
    n = 6
    print(sum_of_natural_numbers_3(n))  # 21
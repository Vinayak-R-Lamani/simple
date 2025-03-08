def check_prime(n):
    # if n < 2:
    #     return False
    # for i in range(2, (n //2) + 1):
    #     if n % i == 0:
    #         return False
    # return True
    return False if n < 2 else all(n % i != 0 for i in range(2, (n // 2) + 1))

if __name__ == "__main__":
    print(check_prime(15))
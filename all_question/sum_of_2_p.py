import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Optimized
        if n % i == 0:
            return False
    return True

def get_prime_list(n):
    return [i for i in range(2, n) if is_prime(i)]  # Start from 2

def sum_of_two_prime(n):
    lst = get_prime_list(n)
    ans = []
    num_dict = {}

    for i, num in enumerate(lst):
        complement = n - num
        if complement in num_dict:
            ans.append((complement, num))  # Store actual prime pair
        num_dict[num] = num  # Store number, not index

    print(ans)  # Print the prime pairs
 # Print the 
   
def can_be_expressed_as_sum_of_two_primes(N):
    for i in range(2, N // 2 + 1):  # Check numbers up to N/2
        if is_prime(i) and is_prime(N - i):  
            print(f"{N} = {i} + {N - i}")  # Print the pair
            return True
    return False
 
    
if __name__ == "__main__":
    n = 74
    # print(can_be_expressed_as_sum_of_two_primes(n))  
    sum_of_two_prime(n)
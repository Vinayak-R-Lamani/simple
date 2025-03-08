def is_Automorphic(n):
    mul = n * n
    lst = [int(x) for x in str(mul)]
    ans = 0
    j = 1
    m = len(str(n))
    for i in range(0, m):
        ans += lst[len(lst) - i - 1] * j
        j *= 10
    print('it is Automorphic number') if n == ans else print('not')
    
def check_automorphic(n):
    square = n * n
    if str(square).endswith(str(n)):
        print(f"{n} is an Automorphic number")
    else:
        print(f"{n} is not an Automorphic number")
    
    
if __name__ == "__main__":
    n = 12
    check_automorphic(n)
    
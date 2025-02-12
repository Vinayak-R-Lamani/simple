import math

def get_factorial(start ,end):
    fact = 1
    for i in range(start , end -1 , -1):
        fact *= i
    return fact
         
def Permutations(n,r):
    return get_factorial(n ,1) // get_factorial(n -r , 1)

def give_Permutation(n,r):
    return math.factorial(n) // math.factorial(n -r)
if __name__ == "__main__":
    ans = give_Permutation(6,4)
    print(ans)
    
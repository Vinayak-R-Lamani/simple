def G_P(a, r,n):
    return a*(r ** n - 1)/ (r -1)

if __name__ == "__main__":
    a , r, n = 1 , 0.5 , 3
    print(G_P(a,r,n))
def find_sum_AP(a , d, n):
    total_sum = 0
    for i in range(n):
        total_sum += a + i * d
    print(total_sum)
    
if __name__ == "__main__":
    a , d ,n = -2,5,8
    find_sum_AP(a,d,n)  # 20
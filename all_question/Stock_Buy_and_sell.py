def best_time_buy_sell(arr:list):
    buy= arr[0]
    total_profit= 0
    for i in range(len(arr)):
        total_profit = max(total_profit , arr[i]-buy)
        buy = min (buy, arr[i])
        
    return total_profit

arr = [90, 80, 70, 60, 50]
ans = best_time_buy_sell(arr)
print(ans)
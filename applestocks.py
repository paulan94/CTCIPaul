#applestocks interviewcake


a = [10,7,5,8,11,9]
b = [-5,-8,-3,-2]

def traderpaul(arr):
    #assuming there are at least 2 prices,
    #which in the case of stocks there should be.
    maxx = a[1] - a[0]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] - arr[i] > maxx:
                maxx = arr[j] - arr[i]
    return maxx


def bettertrader(arr):
    min_price = arr[0]
    max_profit = arr[1]-arr[0]
    
    for curr in arr[1:]:
        max_profit = max(max_profit,curr-min_price)
        min_price = min(min_price,curr)
        print (max_profit)
    return max_profit


print (bettertrader(a))
    

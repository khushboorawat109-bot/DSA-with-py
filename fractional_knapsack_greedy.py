def Fractional_knapsack(items_wt, price,capacity):
    n=len(items_wt)
    items=[ (price[i] , items_wt[i] , price[i]/items_wt[i]) for  i in range(n) ]
    
    for i in range(n):
        for j in range(i+1 , n):
            if(items[i][2] < items[j][2]):
                items[i],items[j]= items[j],items[i]
    profit=0.0

    for price, items_wt,perkgPrice in items:
        if(capacity==0):
            return profit
        if(items_wt <= capacity):
            capacity=capacity-items_wt
            profit=profit+price
        else:
            profit=profit +perkgPrice*capacity
            capacity=0
    print("Total Profit=",profit)

price=[24,21,12,10]
items_wt=[7,3,4,5]
capacity=20
Fractional_knapsack(items_wt,price,capacity)    


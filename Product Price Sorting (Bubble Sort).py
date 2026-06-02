prices = [1200, 500, 2500, 800]
for i in range(len(prices)):
    for j in range(len(prices)-i-1):
        if prices[j] > prices[j+1]:
            prices[j], prices[j+1] = prices[j+1], prices[j]
print(prices)
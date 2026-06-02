n = int(input())
products = []
for i in range(n):
    products.append(int(input()))
search_id = int(input())
if search_id in products:
    print("Found at Index", products.index(search_id))
else:
    print("Product Not Found")
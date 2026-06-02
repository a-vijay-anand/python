a=[12,2,7,9,21,36,4,1]
k = 2
k = k % len(a)
rotated = a[k:] + a[:k]
print(rotated)
scores = [88, 72, 95, 60, 81]
for i in range(len(scores)):
    min_index = i
    for j in range(i+1, len(scores)):
        if scores[j] < scores[min_index]:
            min_index = j
    scores[i], scores[min_index] = scores[min_index], scores[i]
print(scores)

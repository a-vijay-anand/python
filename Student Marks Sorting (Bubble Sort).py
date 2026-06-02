marks = [75, 90, 65, 85, 70]
for i in range(len(marks)):
    for j in range(len(marks)-i-1):
        if marks[j] > marks[j+1]:
            marks[j], marks[j+1] = marks[j+1], marks[j]
print(marks)
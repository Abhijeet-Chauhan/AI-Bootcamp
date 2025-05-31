dict = {"math":76,"ai":76}

sum = 0

for values in dict.values():
    sum += values

avg = sum / len(dict)
print(avg)
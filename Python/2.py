num = int(input("Number: "))

fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print("Factorial:", fact)
Number = 600851475143
count = 2
while Number > count:
    if Number % count == 0:
        Number = Number / count
    else:
        count = count + 1
print(count)
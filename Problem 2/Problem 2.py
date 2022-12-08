Fn = []
Fn.append(1)
Fn.append(2)
SUM = 0
while Fn[-1]<4E6:
    if Fn[-1] % 2 == 0:
        SUM = SUM + Fn[-1]
    Fn.append(Fn[-1]+Fn[-2])
print(SUM)
count = 1
SUM = 0
NN = int(input())
print("Natural Number is ",NN)
while 3*count < NN:
    SUM = SUM + count*3
    if 5*count < NN:
        if count % 3 != 0:
            SUM = SUM + count*5
    count = count + 1
print("SUM is ",SUM)
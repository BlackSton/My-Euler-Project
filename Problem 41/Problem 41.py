import numpy as np

def number_digit(digits):
    total_number = Factoris(digits)
    arr_temp = np.zeros(digits-1)
    arr = np.zeros(digits-1)
    result_temp = 0
    for i in range(total_number-1):
        arr_temp[-1] += 1
        for j in range(digits-1):
            if arr_temp[-1-j] > j+1:
                arr_temp[-2-j] += 1
                arr_temp[-1-j]  = 0
        result = Make_number(Shake(np.linspace(1,digits,digits),arr_temp))
        if isprime(int(result)) == True:
            print(result)
            if result > result_temp:
                result_temp = result
        else:
            if i % 1000 == 0:
                print('{0:0.2f}%'.format(100*i/total_number))
    return result_temp

def Factoris(N):
    if N == 1:
        return 1
    return N*Factoris(N-1)

def Make_number(data):
    length = len(data)
    number = 0
    for i in range(length):
        number += 10**(length-i-1) * data[i]
    return number

def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def Shake(number,changes):
    Length = len(changes) + 1
    for change in changes:
        change = int(change)
        number[-Length],number[-Length + change] = number[-Length + change],number[-Length]
        Length = Length - 1
    return number
        


print("result: ",number_digit(7))
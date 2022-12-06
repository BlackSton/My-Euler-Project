
def number_digit(count):
    while(count != 0):
        count = count - 1

def power(N):
    if N == 1:
        return 1
    return N*power(N-1)


def Shake(number,changes):
    Length = len(changes) + 1
    for change in changes:
        number[-Length],number[-Length + change] = number[-Length + change],number[-Length]
        Length = Length - 1
    return(number)
        
        
Number = [1,2,3,4]
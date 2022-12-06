import numpy as np

def istriangle_number(n):
    estimate = (-1+np.sqrt(1+8*n))/2
    if abs(int(estimate) - estimate) < 1e-6:
        return True
    else:
        return False

def run():
    Total_Numbers = 0
    for word in words:
        number = 0
        for alphabet in word:
            if alphabet != '"':
                number += ord(alphabet) - 64
        if istriangle_number(number):
            Total_Numbers += 1
    print("Total number of Triangles words : {0}".format(Total_Numbers))

words = np.loadtxt("Problem 42\p042_words.txt",dtype = str,delimiter=',')
run()


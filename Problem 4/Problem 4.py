import numpy as np
def test(k):
    t = []
    for count in range(6):
        t.append(k%10)
        k = k - t[-1]
        k = k/10
    for count in range(3):
        if t[count] != t[-1*(count+1)]:
            break
        else:
            if count == 2:
                print(i*j)
            
for i in np.arange(900,1000,1):
    for j in np.arange(900,1000,1):
        test(i*j)

        
import numpy as np

lst = []
for i in range(1, 121, 2):
    lst.append(i)

for i in range(2, 121, 2):
    lst.append(i)

print(np.array(lst))
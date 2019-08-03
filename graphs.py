import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(12, 12))


def do(x):
    ding = [[0 for i in range(x+1)] for j in range(x+1)]
    ding[0][0] = 1
    ding[1][1] = 1
    for i in range(2, x+1):
        for j in range(0, x+1):
            ding[i][j] = 2 * ding[i - 1][j - 1] - ding[i - 2][j]
    return ding

j = do(8192)

k = []

mod = 7

for x in range(len(j)) :
    k.append([])
    for y in j[x] :
        k[x].append(y%mod)

#l = []

#for x in range(len(k)) :
#    l.append([])
#    for y in k[x] :
#        if (y == 0) :
#            l[x].append("white")
#        else :
#            l[x].append("black")
#fig, axs =plt.subplots(2,1)
#axs[0].axis('tight')
#axs[0].axis('off')
#axs[0].table(cellColours=l, loc='top')
#axs[1].plot([1], [1])

#plt.savefig("C:\Users\Neil Malur\Downloads\trigpolymod" + str(mod) + ".png", bbox_inches='tight')
#plt.show()

plt.imshow(np.array(k))
plt.savefig("C:/Users/Neil Malur/Downloads/trigpolymod" + str(mod) + ".png", bbox_inches='tight')
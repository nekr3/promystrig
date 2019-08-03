import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(24, 24))


def do(x):
    ding = [[0 for i in range(x+1)] for j in range(x+1)]
    ding[0][0] = 0
    ding[1][0] = 1
    for i in range(2, x):
        for j in range(0, x+1):
            ding[i][j] = 2 * ding[i - 1][j - 1] - ding[i - 2][j]
    return ding

j = do(1000)

k = []

mod = 5

for x in range(len(j)) :
    k.append([])
    for y in j[x] :
        k[x].append(y%mod)

plt.imshow(np.array(k))
plt.savefig("/media/hdd0/unraiddisk1/student/neilm/promystmp/sinepolytinymod" + str(mod) + ".png", bbox_inches='tight')

import time
import random
# 初始化一个n点的完全图，每条边染白色
def CreateG(n):
    V = []
    G = {}
    for i in range(n):
        V.append(i)
    for i in range(n):
        for j in range(i + 1, n):
            r = random.random()
            if r > 0.5:
                G[(i, j)] = 'red'
            else:
                G[(i, j)] = 'blue'

    return V, G

# 返回完全图Kn中的所有K4
def CreateK4(V, G):
    K4 = []
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            for k in range(j + 1, len(V)):
                for l in range(k + 1, len(V)):
                    subG = {(i,j):G[(i,j)], (i,k):G[(i,k)], (i,l):G[(i,l)], (j,k):G[(j,k)],(j,l):G[(j,l)], (k,l):G[(k,l)]}
                    K4.append(subG)
    return K4

# 判断K4是否是单色的
def ismonoK4(subG):
    L = [color for color in subG.values()]
    count = 1 if len(set(L)) == 1 else 0
    return count

# 计算Kn中单色K4的数目
def CntmonoK4(V, G):
    cnt = 0
    monoG = []
    K4 = CreateK4(V, G)
    for subG in K4:
        if ismonoK4(subG):
            cnt += 1
            monoG.append(subG)
    return cnt, monoG


def DrawG():
    pass


if __name__ == '__main__':
    s = time.time()
    n = 10
    V, G = CreateG(n)
    Mostcnt = n * (n - 1) * (n - 2) * (n - 3) / 24 * 2 ** (-5)
    K4cnt = Mostcnt
    #print(Mostcnt)
    while K4cnt >= Mostcnt:
        K4cnt, monoG = CntmonoK4(V, G)
        #print(K4cnt)

    print("n = {}时，通过随机法，找到一种染色方法使得完全图中共有{}个同色的K4".format(n, K4cnt))

    if K4cnt > Mostcnt:
        print("未找到一种染色方法使得同色的K4个数不大于n选4*2e-5：{}".format(Mostcnt))
    else:
        print("找到一种染色方法使得同色的K4个数不大于n选4*2e-5：{}".format(Mostcnt))
    #if len(monoG) > 0:
    #    print("同色的K4为：{}".format(monoG))
    e = time.time()
    print('time:{}'.format(e - s))

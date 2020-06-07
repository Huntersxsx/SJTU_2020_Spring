import random
import math
from itertools import product


T = 200.0  # 温度
Anneal_rate = 0.99   # 退火率
NumIter = 200  # 总迭代次数
Balance = 100  # 某一温度下循环次数
Weight = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118,120]  # 每个物品的重量
Value = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]  #每个物品的价值
Capacity = 750  # 背包总容量
NumItem = len(Weight) # 物品个数


# 赋值函数 把B列表元素赋值给A列表
def cop(A, B):
    for i in range(len(A)):
        A[i] = B[i]

# 计算当前方案的总价值和总重量
def CalValueWeight(solution):
    TotalValue = 0
    TotalWeight = 0
    for i in range(len(solution)):
        TotalValue += solution[i] * Value[i]
        TotalWeight += solution[i] * Weight[i]
    return TotalValue, TotalWeight

# 随机产生初始解
def InitSolution():
    initsolution = [0] * NumItem
    while (1):
        for i in range(NumItem):
            initsolution[i] = 1 if (random.random() < 0.5) else 0
        TotalValue, TotalWeight = CalValueWeight(initsolution)
        if (TotalWeight <= Capacity): break;
    profits = TotalValue
    return initsolution, profits

# 随机将背包中已经存在的物品取出
def OutItem(solution):
    while (1):
        item = random.randint(0, NumItem - 1)
        if (solution[item] == 1): solution[item] = 0;break;

# 随机放入背包中不存在的物品
def InItem(solution):
    while (1):
        item = random.randint(0, NumItem - 1)
        if (solution[item] == 0): solution[item] = 1;break;

# 一种温度下迭代Balance次后获得的方案
def GenerateSolution(initsolution, profits, T):
    currentsolution = [0] * NumItem  # 当前最好的方案
    tempsolution = [0] * NumItem  # 用于迭代的方案
    originsolution = [0] * NumItem  # 每次迭代前原始的方案
    cop(tempsolution, initsolution)
    currentprofits = profits
    # 迭代Balance次
    for i in range(Balance):
        cop(originsolution, tempsolution)
        item = random.randint(0, NumItem - 1) # 随机选取某个物品
        # 在背包中则将其拿出，并加入其它物品
        if (tempsolution[item] == 1):
            InItem(tempsolution)
            tempsolution[item] = 0
        else:  # 不在背包中则直接加入或替换掉已在背包中的物品
            if (random.random() < 0.5):
                tempsolution[item] = 1
            else:
                OutItem(tempsolution)
                tempsolution[item] = 1
        currentvalue, currentweight = CalValueWeight(tempsolution)
        if (currentweight > Capacity): # 非法解，跳过
            cop(tempsolution, originsolution)
            continue
        if (currentvalue > currentprofits):  # 接受新的解
            cop(currentsolution, tempsolution)
            currentprofits = currentvalue
        else:
            r = 1.0 * (currentvalue - currentprofits) / T
            if (random.random() < math.exp(r)):  # 概率接受劣解
                cop(currentsolution, tempsolution)
                currentprofits = currentvalue
    return currentsolution, currentprofits

# 穷举，遍历所有方案寻找最优方案
def FindOptim():
    solutions = {}
    # 遍历所有方案
    for i in product(range(2), repeat=NumItem):
        solution = list(i)
        profits, weight = CalValueWeight(solution)
        if weight <= Capacity:
            solutions[str(solution)] = profits
    optimprofit = max(solutions.values())  # 满足约束条件的方案中profits的最大值
    optimsolution = list(solutions.keys())[list(solutions.values()).index(optimprofit)] # 满足约束条件的方案中profits最大的方案
    return optimprofit, optimsolution

def Annealing(T):
    solution, profits = InitSolution()
    isOptim = 0
    optimprofit, optimsolution = FindOptim()
    print('通过穷举法，可以获得问题的最优解为{}'.format(optimprofit))
    print('最优的方案为{}'.format(optimsolution))
    for i in range(NumIter):
        solution, profits = GenerateSolution(solution, profits, T)
        T = T * Anneal_rate  # 温度下降
        if (profits == optimprofit):
            print('模拟退火算法迭代{}次后，找到最优解:{},'.format(i + 1, optimprofit))
            isOptim = 1
            break  # 达到最优解提前退出

    if (isOptim == 0):   print('模拟退火算法迭代{}次后，只找到次优解:{},'.format(NumIter, profits));
    print('模拟退火算法得到的方案为：', solution)
    TotalValue, TotalWeight = CalValueWeight(solution)
    print('背包使用了{}/{}'.format(TotalWeight, Capacity))

if __name__ == '__main__':
    Annealing(T)


import math  # 仅用于调用math.sqrt求解平方根
import time  # 仅用于计算运行时间


# 生成增广矩阵[A|b]
def GenerateMatrix(n = 30):
    A = [[] for _ in range(n)]
    A[0] =[6, 1] + (n - 2) * [0] + [7]
    A[-1] = (n - 2) * [0] + [8, 6] + [14]
    for i in range(1, n-1):
        A[i] = (i - 1) * [0] + [8, 6, 1] + (n - i - 2) * [0] + [15]
    return A

# 1范数
def Norm_1(x, y):
    norm = 0
    for i in range(len(x)):
        norm += abs(y[i] - x[i])
    return norm

# 2范数
def Norm_2(x, y):
    norm = 0
    for i in range(len(x)):
        norm += (y[i] - x[i]) ** 2
    return math.sqrt(norm)

# 无穷范数
def Norm_infinity(x, y):
    max_x = 0
    for i in range(len(x)):
        if max_x < abs(x[i] - y[i]):
            max_x = abs(x[i] - y[i])
    return max_x

# 顺序高斯消元法
def Sequential_Gaussian(n = 30):
    A = GenerateMatrix(n)  # 生成n阶系数矩阵
    x = [0] * n  # 初始化解为n维0向量
    # 消元过程
    for k in range(n):
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]   # 计算比值m
            for j in range(k, n):
                A[i][j] -= m * A[k][j]   # 更新a
            A[i][-1] -= m * A[k][-1]   # 更新b
    # 回代过程
    # print(A)
    x[-1] = (A[n - 1][-1] / A[n - 1][n - 1])
    for k in range(n-2, -1 ,-1):
        s = 0
        for j in range(k + 1, n):
            s += A[k][j] * x[j]   # 求和
        x[k] = (A[k][-1] - s) / A[k][k]
    return x

# 追赶法
def Chasing(n = 30):
    A = GenerateMatrix(n)  # 生成n阶系数矩阵
    x = [0] * n  # 初始化解为n维0向量
    a = [0] + [8] * (n - 1); b = n * [6]; c = [1] * (n - 1) + [0]
    alpha = [0] * n; beta = [0] * n; y = [0] * n  # 定义alpha, y, beta为n维向量
    # alpha, y, beta的初值
    alpha[0] = b[0]
    y[0] = A[0][-1] / alpha[0]
    beta[0] = c[0] / alpha[0]
    # 追 过程
    for i in range(1, n):
        alpha[i] = b[i] - a[i] * beta[i - 1]  # 更新alpha
        y[i] = (A[i][-1] - a[i] * y[i - 1]) / alpha[i]  # 更新y
        beta[i] = c[i] / alpha[i]   # 更新beta
    # 赶 过程
    x[-1] = y[-1]
    for i in range(n - 2, -1, -1):
        x[i] = y[i] - beta[i] * x[i + 1]
    return x

# 列主元素消元法
def Col_Gaussian(n = 30):
    A = GenerateMatrix(n)  # 生成n阶系数矩阵
    x = [0] * n  # 初始化解为n维0向量
    # 消元过程
    for k in range(n - 1):
        max_x = 0; idx = 0
        for i in range(k, n):
            if max_x < abs(A[i][k]):
                max_x = abs(A[i][k]); idx = i  # 找出第k列元素最大的行
        if idx != k:
            for j in range(k, n):
                A[k][j], A[idx][j] = A[idx][j], A[k][j]   # 交换系数矩阵的行
            A[k][-1], A[idx][-1] = A[idx][-1], A[k][-1]  # 交换b的行
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]   # 计算比值m
            for j in range(k + 1, n):
                A[i][j] -= m * A[k][j]   # 更新a
            A[i][-1] -= m * A[k][-1]    # 更新b
    # 回代过程
    x[-1] = A[-1][-1] / A[-1][-2]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += A[i][j] * x[j]   # 求和
        x[i] = (A[i][-1] - s) / A[i][i]
    return x

# Jacobi迭代法
def Jacobi_iter(n = 30, error = 1e-5):
    A = GenerateMatrix(n)
    x = [0] * n; x_next = [0] * n
    iter_num = 0
    x_next = Jacobi_loop(n, A, x, x_next)
    while (Norm_1(x, x_next) > error):
    #while iter_num < 10000:
        x = [i for i in x_next]
        iter_num += 1
        x_next = Jacobi_loop(n, A, x, x_next)
    return x_next, iter_num + 1

# Jacobi迭代法中的循环部分
def Jacobi_loop(n, A, x, x_next):
    for i in range(n):
        s1 = 0; s2 = 0
        for j in range(n):
            if j < i:
                s1 += A[i][j] * x[j]
            elif j > i:
                s2 += A[i][j] * x[j]
        x_next[i] = (A[i][-1] - s1 - s2) / A[i][i]
    return x_next

# 高斯-赛德尔迭代法
def Gauss_Seidel_iter(n = 30, error = 1e-5):
    A = GenerateMatrix(n)
    x = [0] * n; x_next = [0] * n
    iter_num = 0
    x_next = Gauss_Seidel_loop(n, A, x, x_next)
    while (Norm_1(x, x_next) > error):
    #while iter_num < 10000:
        x = [i for i in x_next]
        iter_num += 1
        x_next = Gauss_Seidel_loop(n, A, x, x_next)
    return x_next, iter_num + 1

# 高斯-赛德尔迭代法中的循环部分
def Gauss_Seidel_loop(n, A, x, x_next):
    for i in range(n):
        s0 = 0; s1 = 0
        for j in range(n):
            if j < i:
                s0 += A[i][j] * x_next[j]
            elif j > i:
                s1 += A[i][j] * x[j]
        x_next[i] = (A[i][-1] - s0 - s1) / A[i][i]
    return x_next

def PrintResult(n, method, error = 1e-5):
    methods = {Sequential_Gaussian: "顺序高斯消元法", Chasing: "追赶法", Col_Gaussian: "列主元高斯消元法", Jacobi_iter: "Jacobi迭代法", Gauss_Seidel_iter: "Gauss_Seidel迭代法"}
    if method in methods.keys():
        x_real = [1] * n
        if method in [Sequential_Gaussian, Chasing, Col_Gaussian]:
            print('阶数取{}时，{}的求解结果：'.format(n, methods.get(method)))
            x= method(n)
        else:
            print('阶数取{}，终止条件为x_k和x_k+1误差的1范数小于{}时，{}的求解结果：'.format(n, error, methods.get(method)))
            x, iter_num = method(n, error)
            print('迭代{}次后'.format(iter_num))
        print('方程组的解为：{}'.format(x))
        print('与精确解误差的1范数为：{}'.format(Norm_1(x, x_real)))
        print('与精确解误差的2范数为：{}'.format(Norm_2(x, x_real)))
        print('与精确解误差的无穷范数为：{}'.format(Norm_infinity(x, x_real)))
    else:
        print('请检查求解方法的名称！')






if __name__ == '__main__':
    start = time.time()
    #PrintResult(100, Sequential_Gaussian)
    PrintResult(100, Chasing)
    #PrintResult(100, Col_Gaussian)
    #PrintResult(100, Jacobi_iter)
    #PrintResult(100, Gauss_Seidel_iter)
    end = time.time()
    print((end - start) * 1000, 'ms')





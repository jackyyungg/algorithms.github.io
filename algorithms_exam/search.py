import numpy as np
import random
import time
import matplotlib.pyplot as plt

def Linear_search(S,x):

    for i in range(len(S)): #每次往下一個直到找到數字
        if S[i] == x:       
            return i 
    return -1

def Binary_search(S,x):


    low = 0
    high = len(S)-1
    while low <= high: 
        mid = int((low + high) / 2) #取中間的數

        if x == S[mid]:
            return mid
        elif x > S[mid]: #如果key比中間大
            low = mid + 1 #將low變成中間+1
        else:             #如果key比中間大
            high = mid - 1 #將high變成中間-1
    return -1

def Fibonacci_search(S, x):
    size = len(S)
     
    start = -1
     
    f0 = 0
    f1 = 1
    f2 = 1

    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
     
     
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if S[index] < x:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif S[index] > x:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (S[size - 1] == x):
        return size - 1
    return None


def line_chart(x_arr, Lin_array, Bin_array, Fib_array):
    y1 = Lin_array 
    y2 = Bin_array
    y3 = Fib_array
    y = [Lin_array, Bin_array, Fib_array]
    plt.plot(x_arr, y[0], label='Linear_search')
    plt.plot(x_arr, y[1], label='Binary_search')
    plt.plot(x_arr, y[2], label='Fibonacci_search')
    plt.legend(title = 'search type')
    plt.show()

def main():
    n = 100 #設定起始size
    Lin_array = []*200
    Bin_array = []*200
    Fib_array = []*200
    x_arr = []
    for i in range(100):

        t1=t2=t3 = 0
        for k in range(5): #執行5次
            S = random.sample(range(1,2000),n) #在1到2000之間取n個數
            S.sort() #將數字按照順序排列
            x = int(random.choice(S)) #在S中隨機選取一個數當key
            
            start = time.perf_counter() #計算開始時間
            result_l = Linear_search(S,x)
            end = time.perf_counter()
            t1 = end - start + t1 #計算經過時間加上前k次的時間

            start = time.perf_counter() #計算開始時間
            result_b = Binary_search(S,x)
            end = time.perf_counter()
            t2 = end - start +t2 #計算經過時間加上前k次的時間

            start = time.perf_counter() #計算開始時間
            result_f = Fibonacci_search(S,x)
            end = time.perf_counter()
            t3 = end - start +t3 #計算經過時間加上前k次的時間
            

        #計算五次平均時間
        t1 = t1/5
        t2 = t2/5
        t3 = t3/5

        x_arr.append(n)
        Lin_array.append(t1)
        Bin_array.append(t2)
        Fib_array.append(t3)
        
        print('arrange: %d ' %n , end = '')
        print('  Linear cost: %f ' % t1 , end = '' )
        print('  Binary cost: %f ' % t2, end = '' )
        print('  Fibonacci cost: %f ' % t3 )

        n = n + 10 #將size+10
    line_chart(x_arr, Lin_array, Bin_array, Fib_array)

main()
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:00:48 2022
File Name : .py
@author: BAESORI

"""
# 버블 append 없이 중복허용하지 않지 쓴것 
import random

def randsort_A(N = 100) :
    A = [0] * (N + 1)
    cnt = 0     # 회전수 
    while( cnt < N) :
        k = random.randint( 1 , N )
        
        if ( A[k] < 1 ) :
            A[k] = k
            cnt += 1
    return A
    
def randsort_A_test( N = 100 ) :
    global A  # print를 안쓰고 효율적으로 variable로 출력하기위함, print 쓰면 variable로 안보임 
    A = randsort_A()
                
    # 확인
    import matplotlib.pyplot as plt
    x = [ k for k in range ( 0, N + 1 ) ]  
    plt.plot(x, A)

# 선택정렬 기본 403p
def selectionSort_A(ary) :

    n = len(ary)
    for i in range ( 0, n-1 ) :
        minIdx = i
        for k in range(i+1, n) :
            if ( ary [ minIdx ] > ary[k] ) :
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    return ary

def selectionSort_A_test() :
    
    dataAry = [188, 162, 168, 120, 50, 150, 177, 105]
    
    print('정렬 전 --> ', dataAry)
    dataAry = selectionSort_A(dataAry)
    print('정렬 후 --->' , dataAry)
    
    
# 선택정렬 응용 TEST 함수 변경 >> 아직은 중복 허용 
def selectionSort_B(ary) :
  
    n = len(ary)
    for i in range ( 0, n-1 ) :
        minIdx = i
        for k in range(i+1, n) :
            if ( ary [ minIdx ] > ary[k] ) :
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    return ary

def randsort_C(N = 100) :
    A = [0] * (N + 1)
    cnt = 0     # 회전수 
    while( cnt < N) :
        k = random.randint( 1 , N )
        A[cnt] = k
        cnt += 1
    return A
    
def selectionSort_B_test(N = 100) :
    dataAry = [0] * (N + 1)
    k = randsort_C() 
    
    
    print('정렬 전 --> ', k)
    dataAry = selectionSort_B(k)
    print('정렬 후 --->' , k)


# 선택정렬 응용 TEST 중복비허용 
def selectionSort_B(ary) :
  
    n = len(ary)
    for i in range ( 0, n-1 ) :
        minIdx = i
        for k in range(i+1, n) :
            if ( ary [ minIdx ] > ary[k] ) :
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]  # 코드 간단히 
        #tmp = ary[i]
        #ary[i] = ary[minIdx]
        #ary[minIdx] = tmp
    return ary

def randsort_C(N = 100) :
    A = [0] * (N + 1)
    cnt = 0     # 회전수 
    while( cnt < N) :
        k = random.randint( 1 , N )
        # if ( k )
        A[cnt] = k
        cnt += 1
    return A

def randsort_D(N = 100) :
    A = [0] * (N + 1)
    cnt = N     # 회전수 
    while( 0 < cnt ) :
        k = random.randint( 1 , N )
        
        if ( A[k] < 1 ) :
            A[k] = cnt
            cnt -= 1
    return A
    
def selectionSort_D_test(N = 100) :
    dataAry = [0] * (N + 1)
    k = randsort_D() 
    
    
    print('정렬 전 --> ',  k)
    dataAry = selectionSort_B(k)
    print('정렬 후 --->' , k)
    

# 퀵정렬 기본 437p
def quickSort(ary) :
    
    n = len(ary)
    if n <= 1 : # 정렬할 리스트의 개수가 1개 이하면
        return ary
    
    pivoat = ary [ n // 2] # 기준값을 중간값으로 지정
    leftAry, rightAry = [], []
    
    for num in ary :
        if num < pivot :
            leftAry.append(num)
        elif num > pivot :
            rightAry.append(num)
    return quickSort(leftAry) + [pivot] + quickSort(rightAry)

# 전역변수 선언부분
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

# 메인 코드 부분
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬후 ---> ', dataAry)
                


def main() :
    randsort_A_test()
    selectionSort_A_test()
    selectionSort_B_test()
    # selectionSort_C_test()
    selectionSort_D_test()
    
if (__name__ == "__main__") :
    main()
    

<<<<<<< HEAD

"""
QUIZ B :
     1 ~ 100까지 중복을 허용하지 않는 난수 100개를 뽑아서 오름차순으로 정렬하는 코드 Solution 5 가지

"""

### 버블 소트, #append 를 안쓰고... 
# array 가 list보다 속도가 훨씬 빠름  
import random

def randsort_A(N = 100) :
    #global cnt
    A = [0] * (N + 1)
    cnt = 0
    while( cnt < N) :
        k = random.randint( 1 , N)
        if( A[k] < 1 ) :
            A[k] = k
            cnt += 1
            return A
    
def randsort_A_test( N = 100 ) :
    global K
    K = randsort_A()
                
    # 확인
    import matplotlib.pyplot as plt
    x = [ k for k in range ( 0, N + 1 ) ]  
    plt.plot(x, K)

def main() :
    randsort_A_test()
    
if (__name__ == "__main__") :
    main()
    
# 버블        
def bubble( dataset ) :
    n = len(dataset)
    for out in range(n-1, 0, -1):
        for cur in range (0, out) :
            if dataset[cur] > dataset[cur+1]:
               dataset[cur],dataset[cur+1] = dataset[cur+1], dataset[cur]
    
    return dataset
    





import random
# r = random.random()
# print('r=', r)

# 1 구상 > 난수 100개 > 난수를 리스트에 넣고 중복제거 > 100이 될때까지 
def rand(N):
    rd = []
    for i in range(100) :
        r = random.randint(1, 100) # 난수발생
        rd.append(r) #난수 저장
    return rd

# if len(rd) == 100 :
    # break
# print(rd)  

# 2 구상 > 난수 100개 > 난수를 리스트에 넣고 셋으로 중복제거 > 100이 될때까지 
# 리스트[값] 
def rand01(N):
    rd = []
    for i in range(100) :
        rd.append( random.randint( 1, 100 ) ) # 난수발생
        srd = set(rd)
        rd = list(srd)
        if len(rd) == 100 :
            break
    return rd
 
# 2-1 셋연산을 쓰지 않고 리스트 안에 있는 데이터 중에서 확인 
def findNum( array, x ) :
    N = len( array )
    for k in range( N ) :
        if ( array[k] == x ):
            return True
    return False

def rand02( N = 100 ):
    rd = []
    cnt = N
    while ( cnt > 0 ) :
        x = random.randint( 1, 100 ) # floating 시간함수 정규분포로 만들 수 있음 
        if ( findNum( rd, x ) ) :
            continue
        else :
            rd.append( x ) 
            cnt -= 1        
    return rd

# 2-2


# 3 최초 구상했던 것  
def rand03(N):
    rd = []
    for i in range(100) :
        rd.append( random.randint( 1, 100 ) ) # 난수발생
        srd = set(rd)
        rd= list(srd) 
        for i in range(100) :
            rd.append( random.randint( 1, 100 ) ) 
            srd = set(rd)
            rd= list(srd)
    return srd

# if len(rd) == 100 :
    # break
# print(rd) 


    
# 1 while 문 예시 sum( 1 , 100 )
def sigma01( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma01_test( N = 100 ):
    for k in range( 1, N ) :
        print( sigma01( k ) )


# 2 while 문 예시 sum( 1 , 100 )
def sigma02( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma02_test( N = 100 ):
    SL = [0] * ( N + 1 )
    print( SL )
    k = 1
    # for k in range( 1, N ) :
    while ( k < ( N + 1 ) ) :
        SL = sigma02( k )
        k = k + 1
    print( SL )


# 3 while 문 예시 sum( 1 , 100 )
def sigma03( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma03_test( N = 100 ):
    SL = [0] * ( N + 1 )
    # print( SL )
    k = 1
    # for k in range( 1, N ) :
    while ( k < ( N + 1 ) ) :
        SL[k] = sigma03( k )
        k = k + 1
    print( SL )



    
    
    
    
    
    
=======

"""
QUIZ B :
     1 ~ 100까지 중복을 허용하지 않는 난수 100개를 뽑아서 오름차순으로 정렬하는 코드 Solution 5 가지

"""

### 버블 소트, #append 를 안쓰고... 
# array 가 list보다 속도가 훨씬 빠름  
import random

def randsort_A(N = 100) :
    #global cnt
    A = [0] * (N + 1)
    cnt = 0
    while( cnt < N) :
        k = random.randint( 1 , N)
        if( A[k] < 1 ) :
            A[k] = k
            cnt += 1
            return A
    
def randsort_A_test( N = 100 ) :
    global K
    K = randsort_A()
                
    # 확인
    import matplotlib.pyplot as plt
    x = [ k for k in range ( 0, N + 1 ) ]  
    plt.plot(x, K)

def main() :
    randsort_A_test()
    
if (__name__ == "__main__") :
    main()
    
# 버블        
def bubble( dataset ) :
    n = len(dataset)
    for out in range(n-1, 0, -1):
        for cur in range (0, out) :
            if dataset[cur] > dataset[cur+1]:
               dataset[cur],dataset[cur+1] = dataset[cur+1], dataset[cur]
    
    return dataset
    





import random
# r = random.random()
# print('r=', r)

# 1 구상 > 난수 100개 > 난수를 리스트에 넣고 중복제거 > 100이 될때까지 
def rand(N):
    rd = []
    for i in range(100) :
        r = random.randint(1, 100) # 난수발생
        rd.append(r) #난수 저장
    return rd

# if len(rd) == 100 :
    # break
# print(rd)  

# 2 구상 > 난수 100개 > 난수를 리스트에 넣고 셋으로 중복제거 > 100이 될때까지 
# 리스트[값] 
def rand01(N):
    rd = []
    for i in range(100) :
        rd.append( random.randint( 1, 100 ) ) # 난수발생
        srd = set(rd)
        rd = list(srd)
        if len(rd) == 100 :
            break
    return rd
 
# 2-1 셋연산을 쓰지 않고 리스트 안에 있는 데이터 중에서 확인 
def findNum( array, x ) :
    N = len( array )
    for k in range( N ) :
        if ( array[k] == x ):
            return True
    return False

def rand02( N = 100 ):
    rd = []
    cnt = N
    while ( cnt > 0 ) :
        x = random.randint( 1, 100 ) # floating 시간함수 정규분포로 만들 수 있음 
        if ( findNum( rd, x ) ) :
            continue
        else :
            rd.append( x ) 
            cnt -= 1        
    return rd

# 2-2


# 3 최초 구상했던 것  
def rand03(N):
    rd = []
    for i in range(100) :
        rd.append( random.randint( 1, 100 ) ) # 난수발생
        srd = set(rd)
        rd= list(srd) 
        for i in range(100) :
            rd.append( random.randint( 1, 100 ) ) 
            srd = set(rd)
            rd= list(srd)
    return srd

# if len(rd) == 100 :
    # break
# print(rd) 


    
# 1 while 문 예시 sum( 1 , 100 )
def sigma01( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma01_test( N = 100 ):
    for k in range( 1, N ) :
        print( sigma01( k ) )


# 2 while 문 예시 sum( 1 , 100 )
def sigma02( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma02_test( N = 100 ):
    SL = [0] * ( N + 1 )
    print( SL )
    k = 1
    # for k in range( 1, N ) :
    while ( k < ( N + 1 ) ) :
        SL = sigma02( k )
        k = k + 1
    print( SL )


# 3 while 문 예시 sum( 1 , 100 )
def sigma03( N = 100 ) :
    S = 0
    k = 1
    while(k < (N + 1) ) :
        S = S + k
        k = k + 1
    return S

def sigma03_test( N = 100 ):
    SL = [0] * ( N + 1 )
    # print( SL )
    k = 1
    # for k in range( 1, N ) :
    while ( k < ( N + 1 ) ) :
        SL[k] = sigma03( k )
        k = k + 1
    print( SL )



    
    
    
    
    
    
>>>>>>> cff14fcb88c7676f9ea7f607d2609465a3892560
    
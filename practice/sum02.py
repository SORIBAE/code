<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:15:18 2022
File Name : .py
@author: BAESORI

"""

"""
 QUIZ B :
     1 ~ 100까지 중복을 허용하지 않는 난수 100개를 뽑아서 오름차순으로 정렬하는 코드 Solution 5 가지
"""



# f01
#-1, 3,-5, 7 ..... 99 의 SUM
# -1 -5 -9..............
#  3  7  11 ............

# an = 4n + 1
# an = 4n + 3


# 하나는 -1,1,-1(짝수홀수 구분) 반복, 또다른 하나는 1, 3, 5, 7, 9 둘을 곱
# 양수 25개, 음수 25개 총 50개  
## B = [0] + [ 2*n - 1 for n in range (1, 50) ]
# 리스트끼리 곱하면 안되고, 리스트의 element 끼리 곱하여
def f01F(N) :   # 모든 경우에 답이 50이 나오는 문제점 
    fN = [0] + [ 2*n - 1 for n in range (1, 51) ]
    fP = [0] + [-1, 1] * 51
    S = 0
    for n in range ( 0, 51 ) :
        S = S + fN[n] * fP[n]        
    return S

def f_test01F():
    N = 51
    S = f01F(N)
    print( "S=", S )

def f01FQ(N) :   # 모든 경우에 답이 50이 나오는 문제점 
    fN = [0] + [ 2*n - 1 for n in range (1, N+1) ]
    fP = [0] + [-1, 1] * (N+1)
    S = 0
    for n in range ( 0, N+1 ) :
        S = S + fN[n] * fP[n]        
    return S

def f_test01FQ():
    N = 50
    for k in range( 1, N + 1 ) :
        S = f01FQ(k)
        print( "S(",k,")=", S, end=' ' )

def f01F1(N) :   # 모든 경우에 답이 50이 나오는 문제점 
    A = [0]*( N + 1 )
    B = [0]*( N + 1 )
    LM = 0
    LP = 0
    for n in range ( 0, N + 1 ) :
        A[n] = - n*4 + -1
        LM += A[n]
        B[n] = n*4 + 3
        LP += B[n]
    
    return LM + LP, LM, LP, A, B

def f_test01F1():
    N = 50
    for k in range( 1, N + 1 ) :
        S = f01F1(k)
        print( "S(",k,")=", S[0], end=' ' )



#
def f01E(N) :
    A = [0]*( N + 1 )
    B = [0]*( N + 1 )
    LM = 0
    for n in range ( 0, N + 1 ) :
        A[n] = - n*4 + -1
        LM += A[n]
    LP = 0
    for n in range( 0, N + 1 ) :
        B[n] = n*4 + 3
        LP += B[n]
    
    return LM + LP, LM, LP, A, B

def f_test01E():
    global A, B
    N = 24
    fsum,LM, LP, A, B = f01E(N)
    print( fsum,LM, LP, "\n" ,A, B  )

def f01E1(N) :
    A = [0]*( N + 1 )
    B = [0]*( N + 1 )
    LM = 0
    for n in range ( 0, N + 1 ) :
        A[n] = - n*4 + -1
        LM += A[n]
    LP = 0
    for n in range( 0, N + 1 ) :
        B[n] = n*4 + 3
        LP += B[n]
    
    return LM + LP, LM, LP, A, B

def f_test01E1():
    global A, B
    N = 50
    for k in range( 1, N + 1 ) :
        S = f01E1(k)
        print( "S(",k,")=", S[0], end=' ' )



def f01D(N) :
    LM = 0
    for n in range ( 0, N + 1 ) :
        An = - n*4 + -1
        LM += An
    LP = 0
    for n in range( 0, N + 1 ) :
        Bn = n*4 + 3
        LP += Bn
    
    return LM + LP, LM, LP

def f_test01D():
    N = 24
    print( f01D(N) )
    
# 리스트로 만들어서 어떻게 도는지, 증명
def f01D_A(N) :
    fM = [0] * (N + 1)
    fP = [0] * (N + 1)
    
    LM = 0
    for n in range ( 0, N + 1 ) :
        An = - n*4 + -1
        fM[n] = An 
        LM += An
        
    LP = 0
    for n in range( 0, N + 1 ) :
        Bn = n*4 + 3
        fP[n] = Bn
        LP += Bn
    
    return LM + LP, LM, LP, fM, fP

def f_test01D_A():
    N = 24
    print( f01D(N) )


def f01C(N) :
    LM = 0
    for n in range ( 0, N + 1 ) :
        A = - n*4 + -1
        LM += A
        
    LP = 0
    for n in range( 0, N + 1 ) :
        B = n*4 + 3
        LP += B
    
    return LM + LP, LM, LP

def f_test01C():
    N = 24
    print( f01C(N) )

#가독성 
def f01B(N) :
    LM = 0
    for A in range ( 0, N + 1 ) :
        LM = LM - A*4 -1
        
    LP = 0
    for B in range( 0, N + 1 ) :
        LP = LP + B*4 + 3
    
    return LM + LP, LM, LP

def f_test01B():
    N = 24
    print( f01B(N) )


 
def f01A(N) :
    A = -1
    B = 3
    
    LM = 0
    for i in range ( 0, N + 1 ) :
        LM = LM - i*4 + A
    
    LP = 0
    for K in range( 0, N + 1 ) :
        LP = LP + K*4 + B
    S = LM + LP
    return S, LM, LP

def f_test01A():
    N = 24
    print( f01A(N) )


def f01(N) :
    LM = -1
    LP =  3
    for i in range (-1, -97,-4) :
        LM = LM + i
    for K in range(3, 99, 4) :
        LP = LP + K
    return LM + LP

def f_test01():
    N = 24
    print( f01(N) )
    
# f02
def f02(N) :
    LM = -1
    LP =  3
    for i in range (-1, -97,-4) :
        LM = LM + i
    for K in range(3, 99, 4) :
        LP = LP + K
    return LM + LP

def f_test02():
    N = 24
    print( f02(N) )
    
def main():
    global A, B
    f_test01()
    f_test02()
    f_test01A()
    f_test01B()
    f_test01C()
    f_test01D()
    f_test01E()
    f_test01D_A()
    f_test01F()
    f_test01G()
    
    
if(__name__ == "__main__") :
    main()

=======
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:15:18 2022
File Name : .py
@author: BAESORI

"""

"""
 QUIZ B :
     1 ~ 100까지 중복을 허용하지 않는 난수 100개를 뽑아서 오름차순으로 정렬하는 코드 Solution 5 가지
"""



# f01
#-1, 3,-5, 7 ..... 99 의 SUM
# -1 -5 -9..............
#  3  7  11 ............

# an = 4n + 1
# an = 4n + 3


# 하나는 -1,1,-1(짝수홀수 구분) 반복, 또다른 하나는 1, 3, 5, 7, 9 둘을 곱
# 양수 25개, 음수 25개 총 50개  
## B = [0] + [ 2*n - 1 for n in range (1, 50) ]
# 리스트끼리 곱하면 안되고, 리스트의 element 끼리 곱하여
def f01F(N) :   # 모든 경우에 답이 50이 나오는 문제점 
    fN = [0] + [ 2*n - 1 for n in range (1, 51) ]
    fP = [0] + [-1, 1] * 51
    S = 0
    for n in range ( 0, 51 ) :
        S = S + fN[n] * fP[n]        
    return S

def f_test01F():
    N = 51
    S = f01F(N)
    print( "S=", S )

def f01FQ(N) :   # 모든 경우에 답이 50이 나오는 문제점 
    fN = [0] + [ 2*n - 1 for n in range (1, N+1) ]
    fP = [0] + [-1, 1] * (N+1)
    S = 0
    for n in range ( 0, N+1 ) :
        S = S + fN[n] * fP[n]        
    return S

def f_test01FQ():
    N = 50
    for k in range( 1, N + 1 ) :
        S = f01FQ(k)
        print( "S(",k,")=", S, end=' ' )

def f01F1(N) :   # 모든 경우에 답이 50이 나오는 문제점 
    A = [0]*( N + 1 )
    B = [0]*( N + 1 )
    LM = 0
    LP = 0
    for n in range ( 0, N + 1 ) :
        A[n] = - n*4 + -1
        LM += A[n]
        B[n] = n*4 + 3
        LP += B[n]
    
    return LM + LP, LM, LP, A, B

def f_test01F1():
    N = 50
    for k in range( 1, N + 1 ) :
        S = f01F1(k)
        print( "S(",k,")=", S[0], end=' ' )



#
def f01E(N) :
    A = [0]*( N + 1 )
    B = [0]*( N + 1 )
    LM = 0
    for n in range ( 0, N + 1 ) :
        A[n] = - n*4 + -1
        LM += A[n]
    LP = 0
    for n in range( 0, N + 1 ) :
        B[n] = n*4 + 3
        LP += B[n]
    
    return LM + LP, LM, LP, A, B

def f_test01E():
    global A, B
    N = 24
    fsum,LM, LP, A, B = f01E(N)
    print( fsum,LM, LP, "\n" ,A, B  )

def f01E1(N) :
    A = [0]*( N + 1 )
    B = [0]*( N + 1 )
    LM = 0
    for n in range ( 0, N + 1 ) :
        A[n] = - n*4 + -1
        LM += A[n]
    LP = 0
    for n in range( 0, N + 1 ) :
        B[n] = n*4 + 3
        LP += B[n]
    
    return LM + LP, LM, LP, A, B

def f_test01E1():
    global A, B
    N = 50
    for k in range( 1, N + 1 ) :
        S = f01E1(k)
        print( "S(",k,")=", S[0], end=' ' )



def f01D(N) :
    LM = 0
    for n in range ( 0, N + 1 ) :
        An = - n*4 + -1
        LM += An
    LP = 0
    for n in range( 0, N + 1 ) :
        Bn = n*4 + 3
        LP += Bn
    
    return LM + LP, LM, LP

def f_test01D():
    N = 24
    print( f01D(N) )
    
# 리스트로 만들어서 어떻게 도는지, 증명
def f01D_A(N) :
    fM = [0] * (N + 1)
    fP = [0] * (N + 1)
    
    LM = 0
    for n in range ( 0, N + 1 ) :
        An = - n*4 + -1
        fM[n] = An 
        LM += An
        
    LP = 0
    for n in range( 0, N + 1 ) :
        Bn = n*4 + 3
        fP[n] = Bn
        LP += Bn
    
    return LM + LP, LM, LP, fM, fP

def f_test01D_A():
    N = 24
    print( f01D(N) )


def f01C(N) :
    LM = 0
    for n in range ( 0, N + 1 ) :
        A = - n*4 + -1
        LM += A
        
    LP = 0
    for n in range( 0, N + 1 ) :
        B = n*4 + 3
        LP += B
    
    return LM + LP, LM, LP

def f_test01C():
    N = 24
    print( f01C(N) )

#가독성 
def f01B(N) :
    LM = 0
    for A in range ( 0, N + 1 ) :
        LM = LM - A*4 -1
        
    LP = 0
    for B in range( 0, N + 1 ) :
        LP = LP + B*4 + 3
    
    return LM + LP, LM, LP

def f_test01B():
    N = 24
    print( f01B(N) )


 
def f01A(N) :
    A = -1
    B = 3
    
    LM = 0
    for i in range ( 0, N + 1 ) :
        LM = LM - i*4 + A
    
    LP = 0
    for K in range( 0, N + 1 ) :
        LP = LP + K*4 + B
    S = LM + LP
    return S, LM, LP

def f_test01A():
    N = 24
    print( f01A(N) )


def f01(N) :
    LM = -1
    LP =  3
    for i in range (-1, -97,-4) :
        LM = LM + i
    for K in range(3, 99, 4) :
        LP = LP + K
    return LM + LP

def f_test01():
    N = 24
    print( f01(N) )
    
# f02
def f02(N) :
    LM = -1
    LP =  3
    for i in range (-1, -97,-4) :
        LM = LM + i
    for K in range(3, 99, 4) :
        LP = LP + K
    return LM + LP

def f_test02():
    N = 24
    print( f02(N) )
    
def main():
    global A, B
    f_test01()
    f_test02()
    f_test01A()
    f_test01B()
    f_test01C()
    f_test01D()
    f_test01E()
    f_test01D_A()
    f_test01F()
    f_test01G()
    
    
if(__name__ == "__main__") :
    main()

>>>>>>> cff14fcb88c7676f9ea7f607d2609465a3892560

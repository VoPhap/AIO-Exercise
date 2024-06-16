import math

def factorial(f):
    result = 1
    if f < 0:
        raise ValueError
    if f == 0 or f == 1:
        return 1
    for i in range(1,f+1):
        result = result*i
    return result    

def approx_cos(x,n) :
    if n <= 0:
        print("n must be greater than zero")
        return
    cos = 0
    for i in range(n+1):
        result = ((-1)**i) * (x**(2*i))/ factorial(2*i)
        cos += result
    return cos

def approx_sin (x,n) :
    if n <= 0:
        print("n must be greater than zero")
        return    
    sin = 0
    for i in range(n+1):
        result = ((-1)**i) * (x**(2*i+1)) / factorial(2*i+1)
        sin += result
    return sin

def approx_sinh (x,n) :
    if n <= 0:
       print("n must be greater than zero")
       return 
    sinh = 0
    for i in range(n+1):
        result = (x**(2*i+1)) / factorial(2*i+1)
        sinh += result
    return sinh

def approx_cosh(x,n):
    if n <= 0:
       print("n must be greater than zero")
       return
    cosh = 0
    for i in range(n+1):
        result = (x**(2*i)) / factorial(2*i)
        cosh += result
    return cosh



assert round ( approx_cos ( x =1 , n =10) , 2) ==0.54
print ( round ( approx_cos ( x =3.14 , n =10) , 2) )

assert round ( approx_sin ( x =1 , n =10) , 4) ==0.8415
print ( round ( approx_sin ( x =3.14 , n =10) , 4) )

assert round ( approx_sinh ( x =1 , n =10) , 2) ==1.18
print ( round ( approx_sinh ( x =3.14 , n =10) , 2) )

assert round ( approx_cosh ( x =1 , n =10) , 2) ==1.54, "you are gay"
print ( round ( approx_cosh ( x =3.14 , n =10) , 2) )





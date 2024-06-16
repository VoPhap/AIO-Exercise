import math

def md_nre (y, y_hat,m,n,p):
    result = 0
    for i in range(1,m+1):
        difference = (y**(1/n)) - (y_hat**(1/n))
        loss = difference ** p
        result += loss
    result = loss / m
    return result
    
md_nre(100,99,1,2,1)
    
    
    



    
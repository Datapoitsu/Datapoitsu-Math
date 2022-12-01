## -------------------- Falling and rising factorials -------------------- ##
#Written by: Aarni Junkkala

import ProductOfSequence as POS

## -- Falling Factorial -- ##

def FallingFactorial(x,n):
    if n < 0:
        return False
    
    if n == 0:
        return 1
    
    if x == 0:
        return 1
    
    if n == 1:
        return x
    
    total = POS.Product(n-1,0,str(x) + "-i")

    return total

## -- Alternative names -- ##

def DescendingFactorial(x,n):
    return FallingFactorial(x,n)

def FallingSequentialProduct(x,n):
    return FallingFactorial(x,n)

def LowerFactorial(x,n):
    return FallingFactorial(x,n)

## -- Rising Factorial -- ##

def RisingFactorial(x,n):
    if n < 0:
        return False
    
    if n == 0 or x == 0:
        return 0
    
    if n == 1:
        return x
    
    total = POS.Product(n-1,0,str(x) + "+i")

    return total

## -- Alternative names -- ##

def PochhammerFunction(x,n):
    return RisingFactorial(x,n)

def PochhammerPolynomial(x,n):
    return RisingFactorial(x,n)

def AscendingFactorial(x,n):
    return RisingFactorial(x,n)

def RisingSequentialProduct(x,n):
    return RisingFactorial(x,n)

def UpperFactorial(x,n):
    return RisingFactorial(x,n)

if __name__ == '__main__':
    for i in range(0,10):
        print(str(i) + ": " + str(RisingFactorial(5,i)))
    for i in range(0,10):
        print(str(i) + ": " + str(FallingFactorial(5,i)))
## -------------------- Factorial -------------------- ##
#Written by: Aarni Junkkala

#Factorial, marked as x! in math.
#Example: 5! = 5*4*3*2*1

def Factorial(n):
    if n < 0:
        return False
    
    if n == 0:
        return 1
    
    total = 1
    for i in range(n):
        total *= (n - i)
    
    return total

if __name__ == '__main__':
    print(Factorial(5))
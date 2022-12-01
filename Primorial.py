## -------------------- Primorial -------------------- ##
#Written by: Aarni Junkkala

import PrimeNumbers as PN

#Calculates Primorial, meaning multiplication with primenumbers.
# Primorial of five is 2*3*5*7*9 = 2310

def Primorial(n):
    #Can't be less than zero.
    if n < 0:
        return False
    
    #Zero returns always one.
    if n == 0:
        return 1
    
    #If there isn't enough primes calculated, then does so.
    if len(PN.primes) < n - 1:
        PN.GetPrime(n)
    
    #Multiplies primes.
    Total = 1
    for i in range(n):
        Total *= PN.primes[i]
        
    return Total

if __name__ == '__main__':
    print(Primorial(5))
## -------------------- Primenumbers -------------------- ##
#Written by: Aarni Junkkala

import math

#Collects primes into a list and returns the prime of that index
primes = [2,3,5] #Has first 3 as it will help optimizing the code.

def CalculatePrime(n): #Returns the n:th prime
    global primes
    #If prime index is already found, returns that
    if n <= len(primes) - 1:
        return primes[n]
    
    num = primes[-1] #Starts from last known prime
    while True:
        num += 2 #Because primes are odd (except number 2), there is no point to check any odd numbers
        if str(num)[-1] == '5': #numbers ending with digit 5 aren't primes (except 5 it)
            num += 2

        #Prime can't be divisible with numbers higher that it's sqrt
        sqrt = int(math.sqrt(num))
                
        isPrime = True    
        for k in range(1,len(primes)): #Doesn't have to test number 2, because num can't be an even number
            if primes[k] > sqrt: #Limiter, so code doesn't test unnecessary numbers.
                break
            if num % primes[k] == 0: #If division goes perfectly onto number,
                isPrime = False #Then it isn't a prime
                break
        
        if isPrime == True: #It was a prime!
            primes.append(num)
            if n == len(primes) - 1: #If enough primes have been calculated,
                return primes[n] #then will break and return the correct prime

def IsPrime(n):
    #Checks cases, where we can see instantly, if number isn't a prime
    if n in [2,5]: #Exceptions
        return True
    sn = str(n) #string n
    if sn[-1] not in ['1','3','7','9']: #Last character must be one of these to be a prime
        return False
    
    global primes
    while len(primes) == 0 or primes[-1] < n:
        CalculatePrime(len(primes))
    
    if n in primes:
        return True
    return False

def PrimeGreaterThan(n):
    #Calculates the prime that is greater than n.
    global primes
    #If we already have prime calculated.
    if len(primes) > 0 and primes[-1] > n:
        for i in range(len(primes)):
            if primes[i] > n:
                return primes[i]
    
    #If we don't
    while primes[-1] < n:
        CalculatePrime(len(primes))
    return primes[-1]

def PrimeLesserThan(n):
    global primes
    
    #Impossible case
    if n < 2:
        return -1 #Returns -1 on impossible numbers
    
    #Get's the prime lesser than n
    if len(primes) > 0 and primes[-1] > n:
        for i in range(1,len(primes)):
            if primes[i] >= n:
                return primes[i-1]
    
    #Calculates primes, till we find one greater than n.
    #TODO: optimize this. There is no reason to calculate prime that is greater than n.
    while primes[-1] < n:
        CalculatePrime(len(primes))
    return primes[-2]

def PrimesFromRange(Smallest = 2,Greatest = 2): #Greatest must be 2 or higher
    global primes
    
    #Fail cases and easy answers.
    if Greatest < 2 or Smallest > Greatest: 
        return []
    
    if Smallest == Greatest:
        if IsPrime(Smallest):
            return [Smallest]
        else:
            return []

    #Looks for primes, if there arent enough already.
    while len(primes) < 0 or primes[-1] < Greatest:
        CalculatePrime(len(primes))
    
    indexS = -1
    indexG = len(primes)

    for i in range(len(primes)): #Looks for indexs of the smallest and largest prime.
        if indexS == -1 and primes[i] >= Smallest:
            indexS = i
        if primes[i] > Greatest and i > 0:
            indexG = i
            break #No need to look furter
    return primes[indexS:indexG]

def PrimesTill(n):
    if n < 2:
        return []
    #Reusing previous function.
    return PrimesFromRange(2,n)
    

def GetPrime(n):
    #Used for matematical usage, where prime1 = fisrt, where as in coding 0 is first.
    global primes
    if n - 1 > len(primes) - 1:
        CalculatePrime(n)
    return primes[n - 1]
    
if __name__ == '__main__':
    #Are they primes?
    print("Is 8 prime: ", IsPrime(8))
    print("Is 11 prime: ", IsPrime(11))
    
    #Get the prime lesser than n
    print("Prime lesser than 15:",PrimeLesserThan(15))
    print("Prime lesser than 13:", PrimeLesserThan(13))
    
    #Gets the prime greater than n
    print("Prime greater than 15:", PrimeGreaterThan(15))
    print("Prime greater than 5:", PrimeGreaterThan(5))
    
    #Gets primes till n is reached
    print("Primes till 15:",PrimesTill(100))
    print("Primes till 1:", PrimesTill(1))

    #Gets the range of primes
    print("Primes from range 100-200:",PrimesFromRange(100,200))
    print("Primes from range 15-35:",PrimesFromRange(13,31))
    print("Primes from range 0-1:",PrimesFromRange(0,1))
    print("Primes from range 7-7:",PrimesFromRange(7,7))

    #Gets the prime that is 10th (smallest number to use is 1)
    print("5th prime (math):",GetPrime(5))
    
    #Gets the prime based on the index, this will return 101st (smallest number to use is 0)
    print("101th prime (programming):",CalculatePrime(100))
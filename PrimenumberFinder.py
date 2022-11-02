## -------------------- Primenumber finder -------------------- ##
#Written by: Aarni Junkkala

#Collects primes into a list and returns the prime of that index
primes = [2] #has two for bace, as it is easier to start from
def FindPrime(i): #i = index
    global primes
    #If prime of the index isn't found, looks for it.
    if i > len(primes) - 1:
        num = primes[-1] + 1 #Starts from the one above last known prime
        while True:
            #Try to divide with every primenumber
            isPrime = True
            for k in range(len(primes)):
                #if answer is integer, then number isn't a prime
                if (num / primes[k]).is_integer() == True:
                    isPrime = False
                    break
            if isPrime == True:
                primes.append(num)
                #If enough primes have been calculated,
                #then will break and return the correct prime
                if i <= len(primes) - 1:
                    break
            num += 1
            
    return primes[i]

if __name__ == '__main__':
    #Test
    for l in range(10):
        print(FindPrime(l))
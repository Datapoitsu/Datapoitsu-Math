## ------------------- Euler's totient function ------------------- ##
#Written by: Aarni Junkkala

# Tests all numbers from 0, to k, returns the total amout of numbers where GCD([n,k]) = 1
import GreatestCommonDivisor as GCD
def ETF(number):
    
    #Can't be negative or zero
    if number <= 0:
        return False
    
    num = 0
    for i in range(1,number):
        if GCD.GCD([i,number]) == 1:
            num += 1
    return num

def phi(numbers):
    return ETF(numbers)

if __name__ == '__main__':
    #Tests and answers
    #print(ETF(10)) #4 -> [1,3,7,9]
    #print(ETF(20)) #8 -> [1,3,5,7,9,11,13,17]
    #print(ETF(9))  #6 -> [1,2,4,5,6,7,8]

    while True:
        print(ETF(int(input("Input parameter for Euler's totient function: "))))

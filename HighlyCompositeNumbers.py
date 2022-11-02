## -------------------- Highly Composite numbers -------------------- ##
#Written by: Aarni Junkkala

import NumberOfDivisorsFunction as NODF
#HCN's are integer that have more divisors than other integers smaller than it.
#note: 1 and 2 aren't HCN's, they will be on the list, but will be excluded, when returning the value.
numbers = [1,2] #highly composite numbers.
divisorScore = 2 #Shows the largest amout of divisors at last one on the list. starts as 2, because it is the amout with number 2
def HCN(i): #i = index
    global numbers, divisorScore
    
    num = numbers[-1] + 1 #The number that we are testing
    while i > len(numbers) - 1:
        #Add Highly Composite numbers to the list, till enough has been found
        #Calculate amount of divisors in num
        divisorCount = NODF.NumberOfDivisorsFunction(num,0)
        if divisorCount > divisorScore:
            numbers.append(num)
            divisorScore = divisorCount
        num += 1
    
    return numbers[i - 1]
if __name__ == '__main__':
    print(HCN(8))

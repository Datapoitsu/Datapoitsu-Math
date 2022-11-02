## -------------------- Number Of Divisors Function -------------------- ##
#Written by: Aarni Junkkala

#Returns the sum of (divisor potency to z)
# 24 is built with: 1 x 24, 2 x 12, 3 x 8, 4 x 6. Total of 8
# Each of the divisors are put on potency of z, when z = 0 then function returns the amount of divisors

def NumberOfDivisorsFunction(n,z):
    ## -- Eliminating impossible situations -- ##
    if n <= 0: #Must be more zero
        return False
    
    if (n/1).is_integer() == False: #Must be an integer
        return False
    
    ## -- Function -- ##
    Divisors = [] #values will be built in a way where lower value is always added to front and higher to back
    num1 = 1 #Lowest end to check
    num2 = n #Highest end to check
    while True:
        #If the lower value has been passed, then higher is returned to lowest of high values and lower will be increased by 1
        if num2 < num1:
            num1 += 1
            if len(Divisors) > 0:
                #if first of the list higher than last, then all possibilities have been looked for.
                if Divisors[0] >= Divisors[-1]:
                    break
                else:
                    #When looking for new set of divisors starting from the last one that is highest, then will be optimized a bit.
                    num2 = Divisors[-1]
            else:
                num2 = n

        if num1 * num2 == n: #Numbers multiplied with eachother does return the wanted number
            #If numbers are the same, then just adds one of then and returns
            if num1 == num2:
                Divisors.append(num2)
                break
            #Numbers are added as smaller to fron and bigger to back. 
            Divisors.insert(0,num1)
            Divisors.append(num2)
            num1 += 1
        
        num2 -= 1 #Lower for every round
        
        #If numbers have reached the opposite end of the list, then all possible solutions have been found
        if len(Divisors) > 0:
            if num1 > Divisors[-1] or num2 < Divisors[0]:
                break
            
    ## -- Potency -- ##
    for i in range(len(Divisors)):
        Divisors[i] **= z
    return sum(Divisors) #Returns the sum, because when z = 0, is equal of len()

def SigmaFunction(n): #Sigma function is one where z = 1
    NumberOfDivisorsFunction(n,1)

if __name__ == '__main__':
    for i in range(1,15):
        print("nro" + str(i) + ": " + str(NumberOfDivisorsFunction(i,0)))
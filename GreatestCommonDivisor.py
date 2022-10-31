## -------------------- Greatest common divisor ------------------------- ##
#Returns the value of the greates common divisor
#Example:  GCD([12,6,15]) -> 3
def GCD(numbers):
    ## ----- Return and Fail conditions ----- ##

    #Must be a list
    if type(numbers) != list:
        return False
    
    #Null list or list of one value returns false
    if len(numbers) == 0 or len(numbers) == 1:
        return False
    
    #If any of the numbers isn't a integer, then return False
    for i in range(len(numbers)):
        if isinstance(numbers[i], float) or isinstance(numbers[i],int):
            if float(numbers[i]).is_integer() == False:
                return False
        else:
            return False

    
    
    ## ----- Singular value returns itself ----- ##
    if len(numbers) == 1:
        return numbers[0]
    
    ## ----- Converts all numbers to positive numbers ----- ##
    for i in range(len(numbers)):
        if numbers[i] < 0:
            numbers[i] *= -1
    
    ## ----- Obvious answers ----- ##
    #If there is zero, return zero
    for i in range(len(numbers)):
        if numbers[i] == 0:
            return 0
    
    #If there is one, return one
    for i in range(len(numbers)):
        if numbers[i] == 1:
            return 1
    
    ## ----- Prosessing the GCD ----- ##
    #Gets the value with lowest value from the list
    Lowest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < Lowest:
            Lowest = numbers[i]
    
    num = Lowest #Num will be the highest common divisor
    while True:
        #Can't be lower than one
        if num == 1:
            return 1
        for i in range(len(numbers)):
            Failed = False #If is true, means that num isn't divisior of the list
            #if not an integer, then reduce the num and new round
            if (numbers[i] / num).is_integer() == False:
                Failed = True
                break
        if Failed == True: #Lowers num and starts a new round
            num -= 1
            continue
        return num
  
if __name__ == '__main__':
    #Tests and answers
    print(GCD([0,100,999])) # = 0
    print(GCD([1,100,999])) # = 1
    print(GCD([1,100,0]))   # = 0
    print(GCD([4,6,8]))     # = 2
    print(GCD([-10,-15]))   # = 5
    print(GCD([1.23, 4.56]))# = False
    print(GCD(["Cat", "Dog"]))# = False
    print(GCD([0]))         # = False
    print(GCD(0))           # = False
    print(GCD("Cat"))     # = False
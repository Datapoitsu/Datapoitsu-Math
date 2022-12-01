## -------------------- Least Common Multiple -------------------- ##
#Written by: Aarni Junkkala

import GreatestCommonDivisor as GCD #Required
def LCM(numbers):
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

    #If any of numbers is zero, return false
    for i in range(len(numbers)):
        if numbers[i] == 0:
            return False

    ## ----- Converts all numbers to positive numbers ----- ##
    for i in range(len(numbers)):
        numbers[i] = abs(numbers[i])
    
    ## ----- Processing itself ----- ##
    #If list is longer than two, code repeats to formula to each number and the result
    num = numbers[0]
    for i in range(1, len(numbers)):
        result = (num * numbers[i]) / (GCD.GCD([num,numbers[i]])) #Formula
        num = result
    return result

if __name__ == '__main__':
    #Tests and answers
    print(LCM([0,100])) # = False
    print(LCM([2,3])) # = 6
    print(LCM([6,4])) # = 12
    print(LCM([-12,5])) # = 60
    print(LCM([2,3,4,5,7])) # = 420
    print(LCM([980,4950]))
    print(LCM([36,20]))
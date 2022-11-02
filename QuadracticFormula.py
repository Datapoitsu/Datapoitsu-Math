## -------------------- Quadractic Formula ------------------------- ##
#Written by: Aarni Junkkala

#Solves quadratic equation. it looks like following: a*x**2 + b*x + c = 0
#If not able to solve the answer, as equation doesn't hit zero line, code will return None
def QuadracticFormula(a,b,c):
    
    part1 = b ** 2 - 4 * a * c
    #Can't sqrt negative numbers, so will return none, meaning that equation doesn't hit zero line at all
    if part1 < 0:
        return None
    
    part2 = part1 ** (1/2)
    
    #3.1 and 3.2 are separeted as, there is possibility of being two answers,
    #because of the plus-minus sign in formula.
    part31 = -b + part2 / 2 * a
    part32 = -b - part2 / 2 * a
    
    #If there is two answers, will return both in an array, other wise will just return the one answer
    if part31 != part32:
        return [part31,part32]
    else: 
        return part31

if __name__ == '__main__':
    print(QuadracticFormula(-5,3,2))
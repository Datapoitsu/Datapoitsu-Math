## -------------------- Perfect Totien number -------------------- ##
import EulersTotientFunction as ETF

#Returns True of False
#Uses the Euler's Totient function till the result is one,
#then if the sum of results make the starting number is true, otherwise false
#Example: PTN(9) -> phi(9) = 6 -> phi(6) = 2 -> phi(2) = 1 -> 9 == 6 + 2 + 1
def PTN(number):
    numbers = []
    numbers.append(ETF.phi(number))
    while numbers[-1] > 1:
        numbers.append(ETF.phi(numbers[-1]))
    
    if sum(numbers) == number:
        return True
    else:
        return False
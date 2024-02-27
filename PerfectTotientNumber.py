## -------------------- Perfect Totien number -------------------- ##
#Written by: Aarni Junkkala
import EulersTotientFunction as ETF

#Returns True of False
#Uses the Euler's Totient function till the result is one,
#then if the sum of results make the starting number is true, otherwise false
#Example: PTN(9) -> phi(9) = 6 -> phi(6) = 2 -> phi(2) = 1 -> 9 == 6 + 2 + 1
def PTN(n):
    numbers = []
    numbers.append(ETF.phi(n))
    while numbers[-1] > 1:
        numbers.append(ETF.phi(numbers[-1]))
    
    if sum(numbers) == n:
        return True
    return False

if __name__ == "__main__":
    print("Perfect Totien Fucntion", 9, PTN(9))
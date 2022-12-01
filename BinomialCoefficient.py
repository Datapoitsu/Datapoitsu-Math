## -------------------- Binomial coefficient -------------------- ##
#Written by: Aarni Junkkala

import Factorial as F

def BinomialCoefficien(n,k):
    return F.Factorial(n) / ((F.Factorial(k)) * (F.Factorial(n-k)))

if __name__ == '__main__':
    print(BinomialCoefficien(10,3))
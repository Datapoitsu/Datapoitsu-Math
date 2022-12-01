## -------------------- Standard Devation -------------------- ##
#Written by: Aarni Junkkala
import math

def Avarage(Data):
    return sum(Data) / len(Data)

def Variance(Data):
    a = Avarage(Data)
    v = 0
    for i in range(len(Data)):
        v += ((Data[i] - a) ** 2)
    v = v / (len(Data) - 1)
    return v

def StandardDevation(Data):
    c = Variance(Data)
    s = math.sqrt(c)
    return s

if __name__ == '__main__':
    D = [5.113,5.258,4.667,4.416,4.069,6.185,4.528,7.018]
    print("Avarage: " + str(Avarage(D)))
    print("Variance: " + str(Variance(D)))
    #StandardDevation(D)
    print("Standard Devation: " + str(StandardDevation(D)))

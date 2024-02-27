## -------------------- Standard Devation -------------------- ##
#Written by: Aarni Junkkala
import math

def Variance(Data):
    a = sum(Data) / len(Data)
    v = 0
    for i in range(len(Data)):
        v += ((Data[i] - a) ** 2)
    return v / (len(Data) - 1)

def StandardDevation(Data):
    return math.sqrt(Variance(Data))

if __name__ == '__main__':
    D = [5.113,5.258,4.667,4.416,4.069,6.185,4.528,7.018]
    print("Avarage: ", sum(D) / len(D))
    print("Variance: " + str(Variance(D)))
    #StandardDevation(D)
    print("Standard Devation: " + str(StandardDevation(D)))

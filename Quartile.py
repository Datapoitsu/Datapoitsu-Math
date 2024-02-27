## -------------------- Quartile -------------------- ##
#Written by: Aarni Junkkala

#Returns the value that is in center of a list, when the list is in order
def Median(Data):
    Data.sort()
    
    if len(Data) % 2 == 1:
        #For odd amount of data, median is data that is located in center
        return Data[int((len(Data) / 2))]
    else:
        #For even amount of data median is avarage of two most center values
        return (Data[int(len(Data) / 2)] + Data[int(len(Data) / 2 - 1)]) / 2

def SecondQ(Data): #Other name for median
    return Median(Data)

#Returns the value that is in center, from the firts half of the list
def FirstQ(Data):
    S = SecondQ(Data)
    
    #Takes the first half
    FirstHalf = []
    for i in range(len(Data)):
        if Data[i] <= S:
            FirstHalf.append(Data[i])
    
    return Median(FirstHalf)

#Returns the value that is in center, from the second half of the list    
def ThirdQ(Data):
    S = SecondQ(Data)
    
    #Takes second half
    SecondHalf = []
    for i in range(len(Data)):
        if Data[i] >= S:
            SecondHalf.append(Data[i])
    return Median(SecondHalf)
    
if __name__ == '__main__':
    D = [51.263,49.46,48.457,50.651,52.455,49.896,50.405,49.949,50.75]
    D.sort()
    print("F: " + str(FirstQ(D)))
    print("S: " + str(SecondQ(D)))
    print("T: " + str(ThirdQ(D)))
## -------------------- Derangements -------------------- ##
#Written by: Aarni Junkkala

#Calculates the amount of possible orders where items aren't on the original position
def Derangement(n):
    if n < 0:
        return False
    
    if n == 0:
        return 1
    
    if n == 1:
        return 0
    
    return (n - 1) * (Derangement(n - 1) + Derangement(n - 2))

print(Derangement(10))
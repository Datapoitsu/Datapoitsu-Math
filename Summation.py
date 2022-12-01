## -------------------- Summation ------------------------- ##
#Written by: Aarni Junkkala

#Use integer for reapeats (n) and index (i) and calculation as string.
#Code uses eval, so for the calculation you can put (n) and (i) as variables

#Doesn't support variables when called from a nother script.

def Summation(n,i,calculation):
    summa = 0
    for i in range(index, n + 1):
        c = eval(calculation)
        summa += c
    return summa

if __name__ == '__main__':
    while True:
        n = int(input("Insert repeats (n): "))      #Example: 5
        index = int(input("Insert index: "))        #Example: 2
        calculation = input("Insert calculation: ") #Example: i * n + 5
        print(Summation(n,index,calculation))           #Example: should return 90

## -------------------- Product of a sequence -------------------- ##
#Written By: Aarni Junkkala

#TODO: Uses eval(), research if it is possible to do without it.

def Product(n,index,calculation):
    Total = 1
    Calc = ""
    for i in range(index, n + 1):
        c = eval(calculation)
        Total *= c
    print(Calc)
    return Total

if __name__ == '__main__':
    while True:
        n = int(input("Insert repeats (n): "))      #Example: 5
        index = int(input("Insert index: "))        #Example: 2
        calculation = input("Insert calculation: ") #Example: i * n + 5
        print(Product(n,index,calculation))           #Example: should return 90    
## -------------------- Fibonacci Sequence -------------------- ##
#Written by: Aarni Junkkala

Sequence = [0,1] #Sequence itself is saved because the values of it are always the same
#Returns the value of fibonacci from the position of n
def Fibonacci(n):
    global Sequence
    #Appends the list with numbers if necessary
    if n > len(Sequence) - 1:
        for i in range(n - len(Sequence) + 1):
            Sequence.append(Sequence[-1] + Sequence[-2])
    return Sequence[n]

#Test
if __name__ == '__main__':
    while True:
        print(Fibonacci(int(input("Input index of the fibonacci number: "))))
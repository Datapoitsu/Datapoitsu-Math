## -------------------- pi -------------------- ##
#Written by: Aarni Junkkala

# pi ≈ 3.141592653589793
#Calculates pi, instances are telling it how accurate it should be.
#Is it usefull, NO, use math.pi instead
#Just a practice TODO: Research more. Is there better way to calculate pi?

#Saves the values, as recalculating is worthless. Using lower instances, will give the same result as the highest
highestInstances = 1
mostAccurate = 1
def pi(instances):
    global highestInstances, mostAccurate
    #Calculation will be eval(), so calculation can be build as a string.
    calculation = "(" + str(mostAccurate) + ")"
    #Looping from the highest to new, so will only calculte things that are necessary.
    for i in range(highestInstances,instances):
        #Every second is plus and every other is minus.
        if i % 2 == 0:
            calculation += "+"
        else:
            calculation += "-"

        calculation += "(1/" + str(1 + (2 * i)) + ")"
        
    score = eval(calculation)
    mostAccurate = score
    score *= 4
    
    if instances > highestInstances:
        highestInstances = instances
        
    return score
if __name__ == '__main__':
    print(pi(1))
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
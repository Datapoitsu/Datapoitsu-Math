## -------------------- Congruence Relation -------------------- ##

#Returns True or False, baced on weather the modulo n of a and b is same
def ConRel(a,b,n):
    if a % n == b % n:
        return True
    else:
        return False
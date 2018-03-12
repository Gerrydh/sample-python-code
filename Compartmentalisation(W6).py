def sumall(upto):
    sumupto = 0
    for i in range(1, upto + 1):
        sumupto = sumupto + i
    return sumupto

print("The sum of the values from 1 to 50 inclusive is: ", sumall(50))  
print("The sum of the values from 1 to 5 inclusive is: ", sumall(5)) 
print("The sum of the values from 1 to 10 inclusive is: ", sumall(10)) 

#gcd = greatest common divisor
def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
        return x

print("GCD of 6 and 15:", gcd(6, 15)) 
z = gcd(221, 323) # dont have to put this in the print line, create new variable- z
print("GCD of 221 and 323:", gcd(221, 323)) 

# Gerard Hanlon, 2018-13-02
# Factorial number is the number multiplied by all of the numbers smaller than it

def sumall(upto):
    sumupto = 0
    for i in range(1, upto + 1):
        sumupto = sumupto + i
    return sumupto 

print("The Factorial Number of the number 5 is: ", sumall(5))
print("The Factorial Number of the number 7 is: ", sumall(7))
print("The Factorial Number of the number 10 is: ", sumall(10))

#different way to do compart.py
def gcd(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    if x == 0:
        return y
    else:
        return x
    
print("GCD of 6 and 15:", gcd(6, 15)) 
z = gcd(221, 323) # dont have to put this in the print line, create new variable- z
print("GCD of 221 and 323:", z)

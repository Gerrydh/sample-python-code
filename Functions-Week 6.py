def sumall(upto):
    sumupto = 0
    for i in range(1, upto + 1):
        sumupto = sumupto + i
    return sumupto

print("he sum of the values from 1 to 50 inclusive is: ", sumall(50))  
print("he sum of the values from 1 to 5 inclusive is: ", sumall(5)) 
print("he sum of the values from 1 to 10 inclusive is: ", sumall(10)) 

# above function replaces the below 2
sum5 = 0
for i in range(1, 6):
    sum5 = sum5 + i
print("The sum of the vaules from 1 to 5 is inclusive: ", sum5)



sum10 = 0
for i in range(1, 11):
    sum10 = sum10 + i
print("The sum of the vaules from 1 to 10 is inclusive: ", sum10)

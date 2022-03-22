n = int(input("insert a Number: "))

fat = 1
for cont in range(2, n+1):
    fat *=  cont
    
print(fat)    

num = int(input("inster t number of temperature: "))

soma = maior = menor = int(input("inster the temperature 1:  "))

for i in range(2 , num +1):
    temp = int(input("Insert tempeture %d: " %i))
    if temp > maior :
        maior = temp 
    if temp < menor:
        menor = temp
    soma  += temp 
    
print("the higher temperure is %g" % maior)
print("the lower temperure is %g" % menor)
print("the mediun temperure is %.2g" %(soma/num))


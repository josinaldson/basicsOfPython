n = int(input("How many sequencies: "))
for i in range(n): 
    soma = 0 
    num = int(input("Insert the number: "))
    while num != 0 : 
        num = int(input("Insert the number: "))
        if (num % 2) == 0:
            soma += num 
    print("sequencia %i = %i" %(i+1, soma ))

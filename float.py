#s= 1/n + 2/(n - 1) + ... + n/ 1

n = int(input("Insert value"))

soma= 0

for i in range(1, n+1):
    soma += i/(n - i + 1) 

print("Soma = ", soma)


area = int(input("Metros quadrados: "))
litros = area//3

if area % 3 > 0:
    litros = litros + 1; 

qtd = litros // 18  

if litros % 3 > 0:
    qtd = qtd + 1; 

valor = qtd * 80

print("Deve-se comprar:",qtd,"latas \nValor de: R$", valor)

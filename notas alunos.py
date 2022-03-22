nota1 = int(input("NOta 1")) 
nota2 = int(input("NOta 2")) 
nota3 = int(input("NOta 3")) 

media = (nota1 + nota2 + nota3)/3

if media >= 7 and media != 10:
    print("aluno aprovado")
    print(media)
elif media < 7 :
    print("aluno reprovado")
    print(media)

if media == 10 :
    print("aluno aprovado 10")
    print(media)

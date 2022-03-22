num = float(input("insert number"))
num2 = float(input("insert number"))

if num == int(num):
    print("number is a integer")
else:
    print("number is not a integer")
    num2 = num % int(num)
    if num2 > 0.5:
        num = int(num) + 1
    else:
        num = int(num)        

print(num)

round(num2)
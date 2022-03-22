from re import A


n = int(input("Enter number: "))
a, b,c = 1,2,3

while a*b*c < n:
    a += 1 
    b += 1
    c += 1

if a*b*c == n:
    print("%i It is a triangle , because %i*%i*%i = %i" %(n, a, b, c,n)) # for int %i or %d # colocar % ==> %% , # to floats %f, #for string = %s 
else:
    print("not a triangle")
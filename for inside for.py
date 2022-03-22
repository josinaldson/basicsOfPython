x = int(input("Insert firt number")) 
y = int(input("Insert second number")) 

for i in range(x,y+1):
    for j in range(x,y+1):
        print(i,"*",j, "=",i*j)
    

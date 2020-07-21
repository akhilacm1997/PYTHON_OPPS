c=4
for i in range(5):
    
    for j in range(c):
        print("*",end="")
    c -=1
    print()
 # another method 
 
for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()

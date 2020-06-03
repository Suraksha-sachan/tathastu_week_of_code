for i in range(5):
    for j in range(10):
        if(j < 5-i):
            print("*", end=" ")
        elif(j>=5+i):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(5):
    for j in range(10):
        if(j <= i):
            print("*", end=" ")
        elif(j >= 9-i):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

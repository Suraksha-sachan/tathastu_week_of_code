num=int(input("Enter number of term in  Series :"))
a = 0
b = 1
if num > 1 :
    for i in range(num):
        print(a,end=" ")
        c = a + b 
        a = b 
        b = c 

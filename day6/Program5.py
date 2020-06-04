def checkfibonacci(n):
            a = 0
            b = 1
            if (n==a or n==b):
                return True
            c = a+b
            while(c<=n):
                if(c == n):
                    return True
                a = b
                b = c
                c = a + b
            return False

num=int(input("ENTER NUMBER : "))
res=checkfibonacci(num)
if(res==True):
    print(num, " is FIBONACCI NUMBER")
else:
    print(num, " is NOT FIBONACCI NUMBER")

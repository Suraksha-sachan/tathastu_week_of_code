def SpiralPrinting(a,m,n):   

    t = 0

    b = m-1

    l = 0

    r = n - 1

    dr = 0

   

    while (t <= b and l <=r):

       

        if dr ==0:

            for i in range(l,r+1):

                print (a[t][i], end=" ")

            t +=1

            dr = 1

           

        elif dr ==1:

            for i in range(t,b+1):

                print (a[i][r], end=" ")

            r -=1

            dr = 2

           

        elif dr ==2:

            for i in range(r,l-1,-1):

                print (a[b][i], end=" ")

            b -=1

            dr = 3

           

        elif dr ==3:

            for i in range(b,t-1,-1):

                print (a[i][l], end=" ")

            l +=1

            dr = 0

 

a = [[1,1,1,1],

     [3,4,4,2],

     [3,4,4,2],

     [3,3,2,2]]

SpiralPrinting(a,4,4)

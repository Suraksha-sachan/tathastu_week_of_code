def suraksha(m,n):
    
  for i in range(m):
    for j in range(n):
        if i==j :
            print("*", end=' ')
        elif i+j==7 :
            print("*", end=' ')    
        else:
            print("", end=' ')
    print()

suraksha(8,8)

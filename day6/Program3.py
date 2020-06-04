def solution(A): 
    m = max(A) 
    if len(A) == 1:
        return 2 if A[0] == 1 else 1    
    l = [0] * m

    for i in range(len(A)):
        if A[i] > 0:
            if l[A[i] - 1] != 1: 
                l[A[i] - 1] = 1

    for i in range(len(l)):
        if l[i] == 0: 
            return i + 1
    return i + 2    

lst=[]
n=int(input("ENTER SIZE OF LIST : "))
for i in range(n):
    ele=int(input("ENTER"+str(i)+ "th ELEMENT : "))
    lst.append(ele)

print("SMALLEST MISSING NUMBER: ",solution(lst))

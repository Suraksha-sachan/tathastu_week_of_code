
lst = []

n = int(input("Enter number of elements : ")) 

for i in range(0, n):

    ele = int(input())

    lst.append(ele)

print(" INPUT LIST IS : ", lst)

 

list1 = list(dict.fromkeys(lst))

print("LIST AFTER REMOVE DUPLICACY : ",list1)

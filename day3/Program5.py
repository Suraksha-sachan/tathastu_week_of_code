def inter(lst1,lst2):
    lst3= [i for i in lst1 if i in lst2]
    return lst3

lst1 = []
n = int(input("Enter number of elements in List 1 : ")) 
for i in range(0, n):
    ele = int(input("ENTER ELEMENT : "))
    lst1.append(ele)
print(" INPUT LIST IS : ", lst1)

 

lst1 = []
n = int(input("Enter number of elements in List 2: ")) 
for i in range(0, n):
    ele = int(input("ENTER ELEMENT : "))
    lst1.append(ele)
print(" INPUT LIST IS : ", lst1)

print("List after intersection : ",inter(lst1,lst2))

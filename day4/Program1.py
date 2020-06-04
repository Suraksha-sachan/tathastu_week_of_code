def count(tuple, ele): 
    count = 0
    for i in tuple: 
        if (i == ele): 
            count = count + 1
    return count     
tuple = (1, 2, 5, 3, 1, 5, 4, 8, 6, 4, 7, 3)
ele=int(input("ENTER ELEMENT TO SEARCH:"))
print(ele,"present in list ",count(tuple, ele),"times") 

def sort0and1(arr, n) : 
    count = 0   
    for i in range(0, n) : 
        if (arr[i] == 0) : 
            count = count + 1
    for i in range(0, count) : 
        arr[i] = 0  
    for i in range(count, n) : 
        arr[i] = 1
          
def print_arr(arr , n) : 
    print( "Array after Sort is ",end = "") 
    for i in range(0, n) : 
        print(arr[i] , end = " ") 
          
lst = [] 
size= int(input("Enter number of elements in List: "))  
for i in range(0, size): 
    ele = int(input("Enter Only 0 and 1:  ")) 
    lst.append(ele)
len = len(lst)     
sort0and1(lst, length) 
print_arr(lst, length)   

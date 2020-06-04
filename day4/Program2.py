def Sort(list):
    length = len(list)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if (list[j][1] > list[j + 1][1]):
                temp = list[j]
                list[j]= list[j + 1]
                list[j + 1]= temp
    return list


list =[['a', 10], ['b', 5], ['c', 20], ['d', 15]]
print(Sort(list))

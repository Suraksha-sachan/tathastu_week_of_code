dic={'a':1,'b':2,'c':2,'d':3}
result = {}
for key,value in dic.items():
    if value not in result.values():
        result[key] = value
print(result)

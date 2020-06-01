dic=student_data = {'id1': {'name': ['suraksha'],'Branch': ['CSE'], 'Year': ['3'],},
 'id2': {'name': ['Sachan'],'Branch': ['CSE'], 'Year': ['3'], },
 'id3': {'name': ['Sachan'],'Branch': ['CSE'], 'Year': ['3'], },
 'id4': {'name': ['suraksha'],'Branch': ['CSE'], 'Year': ['3'], },}


result = {}

for key,value in dic.items():
    if value not in result.values():
        result[key] = value

print(result)

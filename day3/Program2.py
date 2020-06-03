string = input("ENTER STRING")

result = []

def permute(data, i, length): 

    if i == length: 

        result.append(''.join(data) )

    else: 

        for j in range(i, length): 

            data[i], data[j] = data[j], data[i] 

            permute(data, i + 1, length) 

            data[i], data[j] = data[j], data[i]  

permute(list(string), 0, len(string)) 

print("Resultant permutations", str(result))

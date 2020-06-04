def replace0with5(number):
              number += suraksha(number)
              return number

             

def suraksha(number):
              result = 0
              a = 1
              if (number == 0):
                           result += (5 * a)
                        
              while (number > 0):
                           if (number % 10 == 0):
                                         result += (5 * a)
                           number //= 10
                           a *= 10    
              return result

n=int(input("ENTER NUMBER: "))      
print(replace0with5(n))

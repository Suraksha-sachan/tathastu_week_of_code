def maximum(houseval, n):
              if n == 0:
                           return 0
               
              value1 = houseval[0]
              if n == 1:
                           return value1

              value2 = max(houseval[0], houseval[1])
              if n == 2:
                           return value2

              max_val = None
              for i in range(2, n):
                           max_val = max(houseval[i]+value1, value2)
                           value1 = value2
                           value2 = max_val
              return max_val

houseval = [6, 7, 1, 3, 8, 2, 4]
n = len(houseval)
print("Maximum loot value : ",maximum(houseval, n))

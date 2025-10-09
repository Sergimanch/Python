num_arr = [1,2,35040032,5,-230302,9,10,3,40]
max = -999999999
for i in num_arr:
    if max<i:
        max = i
print(f"El mayor numero del array es: {max}")

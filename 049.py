dupes_arr = [1,2,1,1,1,4,7,4,2]
new_arr = []
for i in dupes_arr:
    if i not in new_arr:
        new_arr.append(i)
print(f"El array sin duplicados es: {new_arr}")
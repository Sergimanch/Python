dicc1 = {"a":2, "b":10, "c":23, "d":5, "f":6}
dicc2 = {"a":7, "b":3, "d":8, "e":9, "c":2}
dicc3 = {}
for i in dicc1:
    if i in dicc2:
        dicc3[i]= dicc1[i] + dicc2[i]
        dicc2.pop(i)
    else:
        dicc3[i]= dicc1[i]
if dicc2.keys != None:
    for j in dicc2:
        dicc3[j] = dicc2[j]
print(dicc3)

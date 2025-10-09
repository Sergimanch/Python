nombres= ["Demir","Fernando","Rodriguez","Cirakoglu","Toyota"]
nombresOrd = []
temp = nombres
while temp:
    min = temp[0]
    for i in temp:
        if i<min:
            min=i
    nombresOrd.append(min)
    temp.remove(min)
print(nombresOrd)
  
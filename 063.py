lista = [1,2,2,1,12,4,53,2,12,4,5,64,3,23,23,54,8,23,5,7,9]
pares = 0
impares = 0
listap=[]
listai=[]
for i in lista:
    if i %2 == 0:
        pares+=1   
        listap.append(i) 
    else:
        impares+=1
        listai.append(i)
print(f"Hay {pares} pares y son {listap} y hay {impares} impares y son {listai}")    




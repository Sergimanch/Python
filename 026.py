num1 = 0
num2 = 1
sum = 0
cifra = int(input("Introduce la cifra de fibonacci que quieres "))
for i in range(cifra):
    print (num1, end=" ")
    sum = num1
    num1 = num2
    num2 = sum + num1
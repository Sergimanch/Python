lado = 7
for i in range(lado):
    leading = ' ' * i
    stars = 2 * (lado - i) - 1
    print(leading + '*' * stars)
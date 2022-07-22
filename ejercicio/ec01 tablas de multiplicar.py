n = int(input("¿Que tabla de multiplicar desea consultar?: "))
print("La tabla del",n, "es")
for m in range (1, 11):
    print ("{:>2} x {} = {:>2}".format(m, n, m*n))
    
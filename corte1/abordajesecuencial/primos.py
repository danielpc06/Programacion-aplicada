#Este ejercicio vale 1 decima para el corte 1 

while True:
    num =input("ingrese un numero: ")
    num=int(num)
    for i in range(1,num+1):
        cont=0
        for n in range(1,i+1):
            residue=i%n
            if residue==0:
                cont=cont+1
    if cont==2:
        print("el numero ingresado es primo.")
    else:
        print("el numero ingresado no es primo")


# nunca nos prohibio usar *
def dividirOper(x, y):
    if(x>y):
        return dividirOper(x-y,y)+1
    elif(x<y):
        return 0
    else:
        return 1

def dividir(x, y):
    res = dividirOper(x,y)
    print("%i / %i = %i, sobra %i"%(x, y, res,x-(res*y) ))

def probarDivisiones():
    dividir(15,6)
    dividir(4,6)
    dividir(500,21)
    dividir(151,32)
    dividir(1024,8)

def encontrarMayor():
    print("Teclea una serie de numeros para encontrar el mayor")
    bandera = True
    max = None
    temp = None
    while(bandera):
        temp = int(input("Teclea un numero [-1 para salir]: "))
        try:
            if(temp == -1):
                bandera = False
            elif(temp >= max):
                max = temp
        except TypeError:
            max = temp
        except ValueError:
            pass
    if(max!=None):
        print("El mayor es: %i"%max)
    else:
        print("No hay valor mayor")

def main():
    bandera = True
    while(bandera):
        print("Mision 07. Ciclos while")
        print("Autor: Emiliano Heredia Garcia")
        print("Matricula: A01377072")
        print("1. Calcular divisiones")
        print("2. Encuentra el mayor")
        print("3. Salir")
        opc = int(input("Teclea tu opcion: "))
        if(opc==1):
            x = int(input("Dividir: "))
            y = int(input("Entre: "))
            dividir(x, y)
        elif(opc==2):
            encontrarMayor()
        elif(opc==3):
            print("Gracias por usar este programa, regresa pronto")
            bandera = False
        else:
            print("ERROR, teclea 1, 2 o 3")

main()
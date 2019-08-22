def problema(numero):
    int(numero)
    if(numero==1):
        print (numero)
        return 0
    elif(numero%2!=0):
        numero=3*numero+1
        print(numero)
        problema(numero)
    elif(numero%2==0):
        numero=numero/2
        print(numero)
        problema(numero)
      
#FUNCION MAIN PARA EJECUTAR LA FUNCION RECURSIVA
if __name__ == "__main__":
    #print("Numero por ingresar")
    #ingreso=input()
    #numero=int(ingreso)
    #Aqui hice un cambio XD
    print("Hola")
    problema(int(22))
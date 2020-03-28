import numpy as np;
def imprimir_matriz(charar):
    for i in range(26):
        for j in range(26):
            print(charar[i][j].decode(), "\t", end='')
        print("\n");
def posicion(caracter):
    Abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Posicion=0
    for i in range(len(Abecedario)):
        if ord(Abecedario[i])==ord(caracter):
            Posicion=i;
            break;
    return Posicion;

def consultar(charar,Y,Z):
    X=0
    for i in range(26):
        if ord(charar[i][Y])==ord(Z):
            X=i;
            break;
    return X
Rta=int(input("Cifrado Vigenere.\n\n1. Cifrar\n2. Descifrar\n\nRta: "))
#Rta=2
if Rta==1:
    #Solicitar Datos
    Texto = input("Por favor introduzca el texto a cifrar: ");
    Clave = input("Por favor introduzca la clave: ");
    #Texto = "To be or not to be that is the question";
    Texto = Texto.upper().strip().replace(" ", "");
    #Clave = "Relations";
    Clave = Clave.upper().strip().replace(" ", "");

    charar = np.chararray((26, 26));
    charar[:] = '*';

    Abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cont=0
    for i in range(26):
        for j in range(26):
            if cont>=26:
                cont=0;
            if cont+i>=26:
                cont=i*-1
            charar[i][j]=Abecedario[cont+i];
            cont+=1;

    #imprimir_matriz(charar)

    #Generar Keyword
    Keyword=np.chararray(len(Texto))
    aux=0
    for i in range(len(Texto)):
        if aux>=len(Clave):
            aux=0
        Keyword[i]=Clave[aux]
        aux+=1

    print("Keyword")
    for i in range(len(Texto)):
        print(Keyword[i].decode()," ", end='')
    print("\nPlaintext")
    for i in range(len(Texto)):
        print(Texto[i]," ", end='')
    print("\n\nCiphertext")

    X=0
    Y=0
    Cifrado=np.chararray((len(Texto)))
    Cifrado[:] = '*';

    for i in range(len(Texto)):
        X = posicion(Keyword[i].decode())
        Y = posicion(Texto[i])
        Cifrado[i]=charar[X][Y];

    for i in range(len(Texto)):
        print(Cifrado[i].decode()," ", end='')
    print("\n")
else:
    #Descifrar
    # Solicitar Datos
    Texto = input("Por favor introduzca el texto a descifrar: ");
    Clave = input("Por favor introduzca la clave: ");
    #Texto = "K S  M  E  H  Z  B  B  L  K  S  M  E  M  P  O  G  A  J  X  S  E  J  C  S  F  L  Z  S  Y";
    Texto = Texto.upper().strip().replace(" ", "");

    #Clave = "RELATIONS";
    Clave = Clave.upper().strip().replace(" ", "");

    charar = np.chararray((26, 26));
    charar[:] = '*';

    Abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cont = 0
    for i in range(26):
        for j in range(26):
            if cont >= 26:
                cont = 0;
            if cont + i >= 26:
                cont = i * -1
            charar[i][j] = Abecedario[cont + i];
            cont += 1;
    # Generar Keyword
    Keyword = np.chararray(len(Texto))
    aux = 0
    for i in range(len(Texto)):
        if aux >= len(Clave):
            aux = 0
        Keyword[i] = Clave[aux]
        aux += 1

    print("Keyword")
    for i in range(len(Texto)):
        print(Keyword[i].decode(), " ", end='')
    print("\nCiphertext")
    for i in range(len(Texto)):
        print(Texto[i], " ", end='')
    print("\n\nPlaintext")

    Z = b'*'
    Y = 0
    X=0
    Descifrado = np.chararray(len(Texto))
    for i in range(len(Texto)):
        Y = posicion(Keyword[i].decode())
        Z = Texto[i]
        X = consultar(charar,Y,Z);
        Descifrado[i]=charar[X][0]

    for i in range(len(Texto)):
        print(Descifrado[i].decode(), " ", end='')
    print("\n")
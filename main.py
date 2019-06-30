def agregarHorizontal(matriz,posicionI,posicionJ,valor):
    contador=0
    if(matriz[posicionI][posicionJ]==0 and matriz[posicionI][posicionJ+1]==0):
        while(contador<2):
            matriz[posicionI][posicionJ]=valor
            posicionJ=posicionJ+1
            contador=contador+1
    elif(matriz[posicionI][posicionJ]==0 and matriz[posicionI][posicionJ-1]==0):
        while(contador<2):
            matriz[posicionI][posicionJ]=valor
            posicionJ=posicionJ-1
            contador=contador+1
    return matriz
def agregarVertical(matriz,posicionI,posicionJ,valor):
    contador=0
    entro=0
    while(contador<2):
        if(matriz[posicionI][posicionJ]==0):
            if(posicionI+1==n):
                if(entro==1):
                    matriz[posicionI][posicionJ]=valor
                return matriz
            else:
                entro=entro+1
                matriz[posicionI][posicionJ]=valor
                contador=contador+1
                posicionI=posicionI+1
                
    return matriz

def recorrerMatriz(matriz,n,m):
    contador=0
    ultimaPos=0
    for i in range(n):
        for j in range(m):
            #print("--entro i : ",i," j : ",j)            
            if(i%2==0):
                if (contador==0):
                    contador=contador+1
                    matriz=agregarHorizontal(matriz,i,j,contador)
                if (matriz[i][j]==0):
                    if(j==m-2 or j==m-1):
                        contador=contador+1
                        #print("entro i : ",i," j : ",j," contador : ",contador)
                        matriz=agregarVertical(matriz,i,j,contador)
                        #print("----- : " ,matriz)
                    else:
                        contador=contador+1
                        matriz=agregarHorizontal(matriz,i,j,contador)
                ultimaPos=j
            elif(i%2!=0):
                if (matriz[i][ultimaPos]==0):
                    if((ultimaPos==0 and i>0) or (ultimaPos==1 and i>0)):
                        contador=contador+1
                        if(matriz[i][ultimaPos]!=0):
                            contador=matriz[i][ultimaPos]
                        matriz=agregarVertical(matriz,i,ultimaPos,contador)
                        #print("------- : ",matriz)
                    else:
                        contador=contador+1
                        matriz=agregarHorizontal(matriz,i,ultimaPos,contador)
                ultimaPos=ultimaPos-1
                
    return matriz

n = 6
m = 6
#a = n*m
matriz = []

for i in range(n):
    matriz.append([])
    for j in range(m):
        matriz[i].append(0)
        #print("valor i : ",i," valor j : ",j)
        #print (matriz)

print(matriz)

matriz = recorrerMatriz(matriz,n,m)
print(matriz)
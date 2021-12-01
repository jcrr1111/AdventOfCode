path= 'Archivo1.txt'
f = open(path, 'r')
aux=[]
contador=0

while True:
    aux1 = f.readline()
    aux1 = aux1.strip('\n')
    if not aux1:
        break
    aux1 = int(aux1)
    aux.append(aux1)

print(aux)
print(len(aux))

for i in range(len(aux)-3):

    if aux[i]+aux[i+1]+aux[i+2] < aux[i+1]+aux[i+2]+aux[i+3]:
        contador=contador+1


print(contador)
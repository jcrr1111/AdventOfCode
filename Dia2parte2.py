path= 'Archivo2.txt'
f = open(path, 'r')
profundidad=0
horizontal=0
objetivo=0

import re
p = re.compile( '[d][o]' )
q = re.compile( '[u]' )
r = re.compile( '[f][o]' )

while True:
    aux1 = f.readline()
    aux1 = aux1.strip('\n')
    if not aux1:
        break

    m = p.match(aux1)
    if m:
        aux1 = aux1.strip('down')
        aux2 = int(aux1)
        objetivo=objetivo+aux2
        print(aux2)
        print("opcion 1")

    m = q.match(aux1)
    if m:
        aux1 = aux1.strip('up')
        aux2 = int(aux1)
        objetivo=objetivo-aux2
        print(aux2)
        print("opcion 2")

    m = r.match(aux1)
    if m:
        aux1 = aux1.strip('forward')
        aux2 = int(aux1)
        horizontal=horizontal+aux2
        profundidad=profundidad+(objetivo*aux2)
        print(aux2)
        print("opcion 3")

print(horizontal*profundidad)
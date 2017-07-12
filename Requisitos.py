import json
import string, re,io
from pprint import pprint

MIN_WORD_SIZE=5
CORRELATION_THRESHOLD = 20

with open('separado.json') as data_file:
    data = json.load(data_file)
    json_dict = data[0]

#pprint(data)
print('Numero de materias: '+str(len(data)))
pprint(data[1])
pprint(data[2])
print(json_dict['titulo'])

topicoLst = ["" for x in range(len(data))]
topicoWrd = ["" for x in range(len(data))]
for i in range(1, len(data)):
   topicoLst[i] = ""
   topicoWrd[i] = []

   materia = data[i]
   if 'topicos' in materia:
       topicos = materia['topicos']
       for topico in topicos:
           topicoLst[i] = topicoLst[i]+" "+re.sub(r'[^\w\s]','',topico)
       topicoLst[i] = topicoLst[i].split()

       #  Remove palavras pequenas
       for word in topicoLst[i]:
           if len(word) >= MIN_WORD_SIZE:
               topicoWrd[i].append(word)
   if len(topicoWrd[i]) > 1:
       pprint(topicoWrd[i][0]+topicoWrd[i][1])

correlacao = [[0 for i in range(len(data))] for j in range(len(data))]
result="source;target;label;type\n"
for i in range(1, len(data)):
    for j in range (1, i):
        if i != j:
            if len(topicoWrd[i]) == 0 or len(topicoWrd[j]) == 0:
                correlacao[i][j] = 0
                correlacao[j][i] = 0
            else:
                aux = 0
                for r in range(0, len(topicoWrd[i])-1):
                    for s in range(0, len(topicoWrd[j])-1):
                        if topicoWrd[i][r] == topicoWrd[j][s]:
                            aux = aux+1
                if aux >= CORRELATION_THRESHOLD:
                    correlacao[i][j]=1
                    #print(data[i]['cod']+";"+data[j]['cod'])
                    result=result+data[i]['cod']+";"+data[j]['cod']+";topico;undirected\n"

with io.open("topicos.csv", 'w') as outfile:
    outfile.write(result)
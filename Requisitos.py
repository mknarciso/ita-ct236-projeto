import json
from pprint import pprint

with open('separado.json') as data_file:
    data = json.load(data_file)
    json_dict = data[0]

#pprint(data)
print('Numero de materias: '+str(len(data)))
pprint(data[1])
pprint(data[2])
print(json_dict['titulo'])
for i in range(1, len(data)):
   materia = data[i]

   topics = materia['topicos']
   pprint(topics)
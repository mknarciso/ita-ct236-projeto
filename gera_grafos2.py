import json
import io
data = open('separado2.json','r')
materias = json.load(data)
data.close

result="source;target;label;type;obs\n"
for i, materia in enumerate(materias):
	if 'requisitos' in materia:
		for j,req in enumerate(materia['requisitos']):
			result+=materia['cod']
			result+=";"
			result+=req
			result+=";requisito;undirected;\n"


with io.open("req2.csv", 'w') as outfile:
    outfile.write(result)
import json
import io
data = open('separado.json','r')
materias = json.load(data)
data.close

result="id;label;titulo\n"
for i, materia in enumerate(materias):
	result+=materia['cod']
	result+=";"
	result+=materia['cod']
	result+=";"
	result+=materia['titulo']
	result+=";\n"

with io.open("nohs.csv", 'w') as outfile:
    outfile.write(result)
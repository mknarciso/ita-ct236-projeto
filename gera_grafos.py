import json
import io
data = open('separado.json','r')
materias = json.load(data)
data.close

result="source;target;label\n"
for i, materia in enumerate(materias):
	if 'requisitos' in materia:
		for j,req in enumerate(materia['requisitos']):
			result+=materia['cod']
			result+=";"
			result+=req
			result+=";requisito\n"
	if 'autores' in materia:
		for k,materia2 in enumerate(materias):
			if 'autores' in materia2:
				if i!=k:
					for a1,aut1 in enumerate(materia['autores']):
						for a2,aut2 in enumerate(materia2['autores']):
							if aut1.strip() == aut2.strip():
								result+=materia['cod']
								result+=";"
								result+=materia2['cod']
								result+=";autores\n"


with io.open("requisitos.csv", 'w') as outfile:
    outfile.write(result)
import re
import json
import io

f = open('materias.txt','r')
emptyline = re.compile('[\s]*\n')
materias = []
parcial = ""

for linee in f:
	line = linee.decode("latin1").encode("utf-8")
	if not emptyline.match(line):
		parcial = parcial + line
	else:
		materias.append(parcial)
		parcial = ""

with io.open('separado.txt', 'w', encoding="ISO-8859-1") as outfile:
    json.dump(materias, outfile)
f.close
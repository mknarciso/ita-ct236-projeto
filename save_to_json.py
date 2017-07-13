import re
import json
import io

f = open('materias_sem_acento.txt','r')
emptyline = re.compile('[\s]*\n')
materias = []
parcial = ""

 
for line in f:
	#line = linee.decode("latin1")
	if not emptyline.match(line):
		#materias.append(line)
		cod = re.search('([A-Z]{3}\-[0-9]{2})[ -]*([A-Z, \-()0-9/]*)', line)
		req = re.search('[Rr]equisito[s]{0,1} *: *([A-Z, \-()0-9/]*).', line)
		item = {'titulo':cod.group(2),'cod': cod.group(1)}
		horas = re.search('[hH]oras [sS]emanais: *([0-9]+) *- *([0-9]+) *- *([0-9]+) *- *([0-9]+)', line)
		alltopics = re.search('[hH]oras [sS]emanais: *[0-9]+ *- *[0-9]+ *- *[0-9]+ *- *[0-9]+\.(.*)[bB]ibliografia', line)
		bibl = re.search('.*[bB]ibliografia *:(.*)\n', line)
		if alltopics:
			reobj = re.compile(' *([^\.]+) *\.', re.IGNORECASE)
			topics = reobj.findall(alltopics.group(1))	
			if topics:
				#print topics
				item.update({'topicos':topics})

		if horas:
			item.update({'horas':{ 
				"teoria":int(horas.group(1)),
				"exercicios":int(horas.group(2)),
				"laboratorio":int(horas.group(3)),
				"individual":int(horas.group(4))
				}})
		else:	
			print cod.group(1)
		if req: 
			each = re.match("([A-Z]{3}\-[0-9]{2})", req.group(1))
			if each:
				reqs = {'requisitos' : re.findall("([A-Z]{3}\-[0-9]{2})", req.group(1))}
				item.update(reqs)
		if bibl:
			auth = re.compile('(([A-Za-z]{3,}) *, *([A-Z]\. *)+)')
			autores = auth.findall(bibl.group(1))
			list_autores = []
			for aut in autores:
				list_autores.append(aut[0].upper().strip())
			#print list_autores
			item.update({'autores':list(set(list_autores))})
		materias.append(item)
		#print materias
		#parcial = parcial + line
		#cod = re.search('[A-Z]{3}\-[0-9]{2}', line)
		#if cod:
		#	print cod.group(0)
		#	materias.append(cod.group(0))
	#else:
		#materias.append(parcial)
		#parcial = ""

#with io.open("separado.json", 'w', encoding="latin1") as outfile:
with io.open("separado.json", 'w') as outfile:
    outfile.write(unicode(json.dumps(materias, ensure_ascii=False)))
    #json.dump(materias, outfile)
f.close
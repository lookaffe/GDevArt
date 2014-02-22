import sys
sys.path.insert(0, 'libs')
from bs4 import BeautifulSoup
import requests, json
from collections import OrderedDict
from operator import itemgetter

def scrape(url):
	r  = requests.get("http://" +url)
	data = r.text
	soup = BeautifulSoup(data)
	dizzi = dict()
	dizzi = siteNav(soup)
	return json.dumps(dizzi)	

def siteNav(cont):
	dizzio = {}
	count=0
	dizzio['type'] = cont.name
	dizzio['size'] = len(str(cont))
	if cont.get('class') is not None:
		dizzio['classes'] = cont.get('class')
	else:
		dizzio['classes'] = []

	if cont.get('id') is not None:
		dizzio['id'] = cont.get('id')
	else:
		dizzio['id'] = None


	print(cont.get('class'))

	
	li=[]
	for elem in cont.children: 												#per tutti i tag
		if elem.name is not None: 											#che non contengano solo stringa
			print ('tag: - ' + elem.name + ' - in - ' + elem.parent.name) 	#stampo il nome e il nome del genitore.
			a=siteNav(elem)
			li.append(a)
	dizzio['children']=li
	dizzio['children-count'] = len(li)
	return dizzio



#in output vedrai i vari tag con i rispettivi padri ed il dizionario completo.

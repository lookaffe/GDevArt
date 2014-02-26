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
	
	li=[]
	for elem in cont.children:
		if elem.name is not None:
			a=siteNav(elem)
			li.append(a)
	dizzio['children']=li
	dizzio['children-count'] = len(li)
	return dizzio
import sys 
import re
import getopt
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser 
import urllib.request



def main():
	args1=sys.argv[1:]
	

	movie_search = '+'.join(args1)
    
	base_url = 'http://www.imdb.com/find?s=all&q='
	url = base_url+movie_search
    
	title_search = re.compile('/title/tt\d+')
	
	
	br = RoboBrowser(history=True)
	br.open	(url)

	#link = br.get_link(url_regex = re.compile(r'/title/tt(.*)/?ref_=fn_al_tt_1'))
	url_regex=re.compile("/title/tt(.*)/?ref_=fn_al_tt_1")
	#print(url_regex)
	res = br.follow_link(url_regex)
	
	
	

	soup = BeautifulSoup(res.read(),"html.parser")

	

#	qtlink = br.find_link(url='trivia?tab=qt&ref_=tt_trv_qu')


	qtres=br.follow_link('trivia?tab=qt&ref_=tt_trv_qu')

	
	qtsoup = BeautifulSoup(qtres.read(),'html.parser')

	print (qtsoup.h1)

	searchFor=raw_input('Type... ')
	

	all_chars=[]
	
	
	
	quote_entry={}
	char_match=qtsoup.find_all("span",class_=re.compile("character"))
	for c in char_match:
		if c.string not in all_chars:
			all_chars.append(c.string)
	
	

	tag =qtsoup.p
	tag.a.decompose()

	ch_match=[]
	for tag in qtsoup.find_all(re.compile('p')):
		if tag.name == 'p':
			ch_match=tag.find_all(text=re.compile(":(.*)"))	
			for allqt in ch_match:
    				if searchFor in allqt:
	    				print (allqt)
    
    

if __name__=='__main__':
	main()




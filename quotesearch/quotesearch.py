import sys 
import re
import getopt
from bs4 import BeautifulSoup
from mechanize import Browser
import urllib2

def getunicode(soup):
	body=''
	if isinstance(soup, unicode):
		soup = soup.replace('&#39;',"'")
		soup = soup.replace('&quot;','"')
		soup = soup.replace('&nbsp;',' ')
		body = body + soup
	else:
		if not soup.contents:
			return ''
		con_list = soup.contents
		for con in con_list:
			body = body + getunicode(con)
	return body



def getQuote(movie_search, quote_prefix):
    
	base_url = 'http://www.imdb.com/find?q='
	url = base_url+movie_search+'&s=all'
    
	title_search = re.compile('/title/tt\d+')
	
	br = Browser()
	br.open(url)
    

	link = br.find_link(url_regex = re.compile(r'/title/tt(.*)/?ref_=fn_al_tt_1'))
	res = br.follow_link(link)

	soup = BeautifulSoup(res.read(),'html.parser')

	qtlink = br.find_link(url='trivia?tab=qt&ref_=tt_trv_qu')

	qtres=br.follow_link(qtlink)
	
	qtsoup = BeautifulSoup(qtres.read(),'html.parser')

	searchFor=quote_prefix
	
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
	    				print allqt

def main():
	args1=sys.argv[1]
	args2 = ""

	arglen = len(sys.argv)

	if arglen > 2:
		args2 = sys.argv[2]

	movie_search = '+'.join(args1)
	
	getQuote(movie_search, args2)

if __name__=='__main__':
	main()

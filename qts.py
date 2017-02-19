import sys 
import re
import getopt

from bs4 import BeautifulSoup
from mechanize import Browser 
import urllib2


class searching_for_quote:
	def __init__(self,mname):
		self.mv_name=mname
		self.movie_search='+'.join(self.mv_name)
		self.base_url='http://www.imdb.com/find?q='
		self.url=self.base_url+self.movie_search+'&s=all'
		self.title_search=re.compile('/title/tt\d+')

	def reachpage(self):
		'''the action of reaching from home-link to the description page of the movie'''
		br = Browser()
		br.open	(self.url)
		link = br.find_link(url_regex = re.compile(r'/title/tt(.*)/?ref_=fn_al_tt_1'))
		res = br.follow_link(link)

		soup = BeautifulSoup(res.read(),"html.parser")
		qtlink = br.find_link(url='trivia?tab=qt&ref_=tt_trv_qu')
		qtres=br.follow_link(qtlink)
		qtsoup = BeautifulSoup(qtres.read(),'html.parser')
		return qtsoup
		
	def searchfor(self,word):
		pass
	def getcharacters(self):
		'''returns the characters credited in the movie'''

		all_chars=[]
		qsoup=self.reachpage()
		char_match=qsoup.find_all("span",class_=re.compile("character"))
		for c in char_match:
			if c.string not in all_chars:
				all_chars.append(c.string)
		return all_chars
	def getdialouge(self,searchFor):
		qsoup=self.reachpage()
		tag =qsoup.p
		tag.a.decompose()

		q_results=[]
		for tag in qsoup.find_all(re.compile('p')):
			if tag.name == 'p':
				ch_match=tag.find_all(text=re.compile(":(.*)"))	
				for allqt in ch_match:
					if searchFor in allqt:
						q_results.append(allqt)
		return q_results


	

'''def main():
	args1=sys.argv[1:]
	s_obj=searching_for_quote(args1)	
	src=raw_input('Type searchterm... ')
	result=s_obj.getdialouge(src)
	for i in result:
		print(i)

 
if __name__ == '__main__':
	main()
	'''




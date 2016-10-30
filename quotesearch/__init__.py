import sys;

from quotesearch import getQuote

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




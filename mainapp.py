from qts import searching_for_quote
import sys


def main():
	args1=sys.argv[1:]

	s_obj= searching_for_quote(args1)	
	src=raw_input('Type searchterm... ')
	result=s_obj.getdialouge(src)
	for i in result:
		print(i)

 
if __name__ == '__main__':
	main()

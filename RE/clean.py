# cleaning function
# take in uncleaned file and write to new file with appropriate substitutions
# and deletion

import argparse
import re
import string

def main():
	parser = argparse.ArgumentParser(description='clean textfile.')
	parser.add_argument('textfile', metavar='T', help='file to clean')
	args = parser.parse_args()
	
	unclean_file = open(args.textfile)
	text = unclean_file.read()
	text = simpleReplace(text)
	text = dominantReplace(text)
	clean_file = open('cleaned.txt', 'w')
	clean_file.write(text)
	

def simpleReplace(s):
	s = re.sub('&', 'and', s)
	#s = re.sub('page [unnumbered]', '', s)
	s = s.translate(None, string.punctuation)
	return s

def dominantReplace(s):
	if ( s.count('with') >= s.count('wyth') ) :
		s = re.sub('wyth', 'with', s) # also with superscript w ^t
	else :
		s = re.sub('with', 'wyth', s)

	if ( s.count('whiche') >= s.count('which') ) :
                s = re.sub('which', 'whiche', s)
	else :
		s = re.sub('whiche', 'which', s)
	
	if ( s.count('eth') >= s.count('yth') ) :
                s = re.sub('yth', 'eth', s)
        else :
                s = re.sub('eth', 'yth', s)
	return s

if __name__ == '__main__':
	main()




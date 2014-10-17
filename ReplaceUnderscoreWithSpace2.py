#!/usr/bin/python
import sys

class StringUtils(object):
	def __init__(self):
		pass

	def ReplaceUnderscoreWithSpace(self, string):
		length = len(string)
		if (length == 1):
			return string
		listOfString  = list(string)
		i = 1
		while (i < length -1 ):
			if (listOfString[i] == "_"):
				listOfString[i] = " "
			i += 1
		return  ''.join(listOfString)

def main():
	stringUtils = StringUtils()
	for arg in sys.argv[1:]:
		print stringUtils.ReplaceUnderscoreWithSpace(arg)

if __name__ == '__main__':
	main()

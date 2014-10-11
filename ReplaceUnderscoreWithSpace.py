#!/usr/bin/python

def ReplaceUnderscoreWithSpace(string):
	length = len(string)
	if(length == 1):
		return string
	listOfString  = list(string)
	i = 1
	while(i < length -1 ):
		if(listOfString[i] == "_"):
			listOfString[i] = " "
		i += 1
	return  ''.join(listOfString)

print ReplaceUnderscoreWithSpace("_foo_bar_")
print ReplaceUnderscoreWithSpace("foo_bar_")
print ReplaceUnderscoreWithSpace("_foo_bar")
print ReplaceUnderscoreWithSpace("_")


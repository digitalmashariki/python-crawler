# print(sys.version_info)
#Runs with python 2.7 as default, incase of python 3.6 I will uncomment and comment as necessary

#Python 2.7
#import urllib

#OR

#if Python 3.6
from urllib.request import urlopen 

#if using python 2.7
#theURLObject = urllib.urlopen('https://www.strathmore.edu/')

#OR

#If using python 3.6
theURLObject = urlopen('https://www.strathmore.edu/')

theHTML = theURLObject.read()


#Python 3.6
#Convert the byte object to string
theHTMLAsString = theHTML.decode(("utf-8"))

#print(type(theHTML.decode("utf-8")))



myCounter = 0
while myCounter < len(theHTMLAsString):
	myCounter = theHTMLAsString.find('http',myCounter)
	if myCounter == -1:
		break
	else:
		print('http found at index',myCounter )
		print (theHTMLAsString[myCounter:myCounter + 30])
		print("")

	myCounter += 30

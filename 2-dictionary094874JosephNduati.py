
# Manual Standard deviation Temperature Calculation for 12 Months with each month 
#having 30 days a month by use of dictionaries and loops

import matplotlib.pyplot as plt
import random
from math import sqrt


months = {1:'Jan',2:'Feb',3:'March',4:'April',5:'May',
6:'June',7:'July',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

oneYearTempValues = {} 

# Populating the above empty dictionary using two nested loops
# first loop iterates 12 months
# second inner loop iterates 30 days in order to generate temperature values for 30 days
# using random.randint library

for x in range(1,13):
	#Populating the dictionary
	oneYearTempValues[months[x]]={}
	for d in range(1,31):
		oneYearTempValues[months[x]][d]= random.randint(18,28)
print()				
print ('A NESTED DICTIONARY CONSISTING OF 12 MONTHS (JAN - DEC) AS OUTER KEYS \n WITH EACH KEY HAVING 30 DAYS OF TEMPERATURE VALUES ')
print()
print(oneYearTempValues)

#Calcultaing the Standard Deviation for each month
#STEPS:
# Calculate the mean for each month
# Then variance:
# 	Subtract the Mean from each day's value and square the result 
#	Square each value and get a total sum (squared differences)
# 	Then work out the average of those squared differences for each month.
# Then finally get the std which is the square root of the variance

monthlyMeansDictionary = {}

theHorizontal = [1,2,3,4,5,6,7,8,9,10,11,12]  #For ploting as months in matplot

theVertical= [] #An empty list to be populated by Standard deviation figures in the loop below

print()
print('The Standard Deviation for each Month')
print()
for myMonth in oneYearTempValues:
	# for dayInMonth in myMonth:
	m = 0
	start = 0 
	summationMonthly = 0
	varianceMonthly = 0
	stdMonthly = 0

	# Getting a sum of Monthly (30 days) temperature Values
	# to be used for mean calulation:
	for x in range (1,31):
		summationMonthly = summationMonthly + oneYearTempValues[myMonth][x]
		
	# Getting the variance of each month
	for q in range (1,31):
		topLine = (((summationMonthly/30)-oneYearTempValues[myMonth][q])**2)
		varianceMonthly = varianceMonthly + topLine
	varianceMonthly = (varianceMonthly/30)
		
	stdMonthly = round(sqrt(varianceMonthly),2)
	theVertical.append(stdMonthly) #creating a list of the standard deviation values
	print(myMonth + ' ' + str(stdMonthly))
	print()

# Plotting
plt.scatter(theHorizontal, theVertical)

plt.title('Nairobi Monthly Temperature(Celsius) Standard Deviation')
plt.xlabel('Month')
plt.ylabel('Temperature Standard Deviation')

plt.show()




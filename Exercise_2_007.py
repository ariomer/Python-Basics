#Exercise-7 with Solution
#Write a Python program to count the number of each character of a text file.

#Inputs:
#abc.txt -
#German Unity Day
#From Wikipedia, the free encyclopedia
#The Day of German Unity (German: Tag der DeutschenEinheit) is the national day of Germany, celebrated on 3 October as a public holiday. It commemorates the anniversary of German reunification in 1990, when the goal of a united Germany that originated in the middle of the 19th century, was fulfilled again. Therefore, the name addresses neither the re-union nor the union, but the unity of Germany. The Day of German Unity on 3 October has been the German national holiday since 1990, when the reunification was formally completed.


import collections
import pprint
file_input = input('File Name: ')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
print(value)
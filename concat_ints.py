#!usr/bin/python

import sys, itertools

class Solution:

	def __init__(self, ints): # Constructor
		self.ints = ints
		self.all = []

	def splitStr(self, ints): # Function to strip white space, split ints
		ints.lstrip()
		self.ints = ints.split()
		return self.ints

	def makeInts(self, ints): # Function to make str => ints; get total permutations
		total = itertools.permutations(self.ints, len(self.ints))
		for i in total:
			i = ''.join(i)
			i = int(i)
			self.all.append(i)
		return self.all

	def maxMin(self, ints): # Function to return a tuple of min/max values
		maximum = max(self.all)
		minimum = min(self.all)
		return (minimum, maximum)

# Prompt user input
print "type ints: "
data = sys.stdin.readline() # Ints are read in as a str

# Driver Code for Solution
test = Solution(data)
test.splitStr(data)
test.makeInts(data)
print(test.maxMin(data))


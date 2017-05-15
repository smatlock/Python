#!usr/bin/python

import sys

class Solution:

	def __init__(self, word): # Constructor
		self.word = word
		self.sub = [0]

	def findSub(self, word): # Function to evaluate substring pattern
		for i in range(len(word)):
			if word[0:i] == word[len(word)-i:len(word)]:
				self.sub.append(word[0:i])
				found = True
		return (self.sub[-1], len(self.sub[-1])) # Returns Tuple(garland word, degree(garland))


	def makeGarland(self, word, N): # Function to return N-fold garland
		N = N + 1
		garland_sub = self.sub[-1] 
		if len(garland_sub) > 0: # Check for garland substring
			if len(garland_sub)*2 > len(word): # For "overlapping garlands" ex: alfalfa
				return (garland_sub*N)
			else: 
				garland_word = word[0:len(garland_sub)+1]*N # For "non-overlapping garlands" ex: onion
				return garland_word[:-1]
			

# Prompt User for word
print "type word: "
data = sys.stdin.readline().strip()

# Driver Code
test = Solution(data)
print(test.findSub(data))
print(test.makeGarland(data, 10)) # print N=10 fold garland word

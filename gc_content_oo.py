#-----------------------------------------#
# Author: Shelby Matlock				          
# Program uses classes to determine		    
# GC content for an input DNA sequence    
#-----------------------------------------#

class FastaSequence:

	def __init__( self, header, sequence ):
		self.header = header
		self.sequence = sequence

	def getHeader(self):
		return self.header

	def getSequence(self):
		return self.sequence

	def getGC_Content(self):
		self.gc = ((self.sequence.count("C") + self.sequence.count("G"))/float(len(self.sequence)))*100
		return str(round(self.gc, 2)) + "%"

import sys, getopt

def main(argv):
	inputfile = argv
	try:
		opts, args = getopt.getopt(argv, "hi:o", ["ifile="])
	except getopt.GetoptError:
		print "test.py -i <inputfile>"
		sys.exit(2)
	for opt, args in opts:
		if opt == '-h':
			print "test.py -i <inputfile>"
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = args
			sequence = []
			with open(inputfile, 'r') as ref:
				read_file = ref.read()
			lines = read_file.splitlines()
			for line in lines:
				line = line.upper()
				if line.startswith(">"):
					header = line
				if not line.startswith(">"):
					sequence.append(line)
					seq = ''.join(sequence)
			my_fasta = FastaSequence(header, seq)
			print "This is the GC content:", my_fasta.getGC_Content() 
	print "Usage:", sys.argv[0], opt, inputfile 


if __name__ == "__main__":
	(main(sys.argv[1:]))






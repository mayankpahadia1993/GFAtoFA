'''

	Author - Mayank Pahadia
	Program - Extract Segments from GFA into a Fasta File

	Run the program - python extractSegmentsIntoFastaFile.py inputfile.GFA outputfile.fa


'''

import sys

if(len(sys.argv)<3):
	print "Please pass the inputfile and outputfile both to the python script"
	print "Example - python extractSegmentsIntoFastaFile.py inputfile.GFA outputfile.fa"
	exit()

inputfile = sys.argv[1]
outputfile = sys.argv[2]
out = open(outputfile,'w')
with open(inputfile) as f:
	for line in f:
		line = line.split('\t')
		if(line[0]=='S'):
			c = '>'+line[1]+'\n'
			out.write(c)
			c = line[2] + '\n'
			out.write(c)

out.close()
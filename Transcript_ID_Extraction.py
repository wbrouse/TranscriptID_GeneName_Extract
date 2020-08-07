#Extracting transcript IDs and gene names from transcriptome fasta
#Script requires call for python, the name of script, and the input fasta file

#After obtaining the off.txt file, it will need to be opened in a text editor to run a find and replace command for the square brackets and single quotation marks.
#This work around should be fixed in the future

import os
import sys

filename = sys.argv[1]					#Defining user input file needed for to run the program as filename


with open(filename , 'r') as ID, open("Headers_only.fa", "w") as Headers:			#Creates txt file with only headers from input fasta file
	for line in ID:
		if line.startswith('>'):
			Headers.write(line)

with open("Headers_only.fa" , "r") as Headers:				#create the T2G.txt outfile that is used by Van's MakeDirMoveDirToDir.py script
	lines = Headers.readlines()
	output = open("T2G.txt", 'w')
	for line in lines:
		data = line.split('|')
		first = (data[0]).replace('>', '')
		sixth = (data[5])
		output.write(f"{first}\t{sixth}\n")
	output.close()

with open("Headers_only.fa" , "r") as Headers:			#create the off.txt outfile that is used by Van's MakeDirMoveDirToDir.py script	
	lines = Headers.readlines()
	output = open("dupoff.txt", 'w')
	for line in lines:
		data = line.split('|')
		sixth = (data[5])
		output.write(f"{sixth}\n")
	output.close()

from collections import OrderedDict

with open('dupoff.txt', 'r') as dupoff:
	lines = (line.rstrip() for line in dupoff)
	unique_lines = OrderedDict.fromkeys((line for line in lines if line))
	out = open('off.txt' ,'w')
	gene = list(unique_lines.keys())
	for line in gene:
		ind = line.split(', ')
		final = (str(ind[0:]))
		out.write((f"{final}\n"))
	out.close()

#!/usr/bin/python
import argparse
import os.path
import sys, getopt
	
__author__ = 'Anurag Bhargava'
__email__ = "anuragb@cisco.com"
__version__ = "1.0"
	
def extract_type(input_file, dst_path, dst_file, type, mode):
	
       	finput=open(input_file, "r")
       	alllines=finput.readlines()
       	finput.close();
       	foutput = 0
	
	output_file = dst_path + dst_file

	if mode == 'False':
		foutput = open(output_file, 'a')
	else:
		foutput = open(output_file, 'w')
	
	print 'type = ' + type
	for eachline in alllines:
		spos = eachline.find(type,)
		first = eachline.split()
		if spos >= 0 and first[0] == type:
       	       		foutput.writelines(eachline)	
			
	foutput.writelines('\n')
	foutput.close
	
	
def extract(argv):
	input_file = ''
	dst_file = ''
	type = 'all'
	mode = ''
	
	try:
		opts, args = getopt.getopt(argv,"hi:o:t:m:",["ifile=","ofile=","type=", "mode="])
	except getopt.GetoptError:
		print 'yang_data_model_catalog.py -i <inputfile> -o <outputfile> -t <type> -m <mode>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'yang_data_model_catalog.py -i <inputfile> -o <outputfile> -t <type> -m <True for overwite or False for append>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			input_file = arg
		elif opt in ("-o", "--ofile"):
			dst_file = arg
		elif opt in ("-t", "--type"):
                        type = arg
		elif opt in ("-m", "--mode"):
                        mode = arg	
                
	print 'Input file is "', input_file            
	print 'Output file is "', dst_file
	print 'Mode is "', mode
	dst_path = './'
	if type == 'all':
       		extract_type(input_file, dst_path, dst_file, 'typedef', 'True')
       		extract_type(input_file, dst_path, dst_file, 'grouping', 'False')
       		extract_type(input_file, dst_path, dst_file, 'identity', 'False')
       	else:
       		extract_type(input_file, dst_path, dst_file, type, mode)
	
if __name__ == "__main__":
	extract(sys.argv[1:])

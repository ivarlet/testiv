#!/usr/bin/env python

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def my_read_function(filename,f_type) :
	record=SeqIO.read(filename, f_type)
	return record

def get_sub_sequence(record,start,end):
	return record.seq[start:end]

def my_parse_function(filename,f_type) :
	parse=SeqIO.parse(filename, f_type)
	return parse

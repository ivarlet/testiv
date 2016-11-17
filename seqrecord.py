#!/usr/bin/env python

from Bio import SeqIO

def my_read_function(filename,f_type) :
	record=SeqIO.read(filename, f_type)
	return record

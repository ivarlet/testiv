#!/usr/bin/env python

from seqrecord import *
from seq import *

if __name__ =="__main__":
	fasta_filename="NC_005816.fna"
	record=my_read_function(fasta_filename, "fasta")
	print '%(GC) : {0}'.format(get_GC_content(record.seq))
	print 'length :', get_len(record.seq)
	gb_filename="NC_005816.gb"
	genbank_record=my_read_function(gb_filename, "genbank")
	#print 'features :', genbank_record.features
	print 'annotation :', genbank_record.annotations["source"]
	
 

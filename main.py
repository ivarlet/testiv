#!/usr/bin/env python
# -*- coding: utf8 -*-
 

from seqrecord import *
from seq import *
from seqfeatures import * 

if __name__ =="__main__":
	#fasta file parsing#
	fasta_filename="NC_005816.fna"
	record=my_read_function(fasta_filename, "fasta")
	print '%(GC) : {0}'.format(get_GC_content(record.seq))
	print 'length :', get_len(record.seq)

	#genbank file parsing"
	gb_filename="NC_005816.gb"
	genbank_record=my_read_function(gb_filename, "genbank")

	print 'features :', genbank_record.features[0]
	#print 'annotation :', genbank_record.annotations["source"]
	
	#work with SeqRecord features (SeqFeature)
	for feature in genbank_record.features[0::5]:
		start,end,strand=get_location(feature)
		if (strand==1):
			strand="+"
		else:
			strand="-"	
		print "this feature ",feature.type," starts at ",start," ends at ",end," on the strand ",strand
#print 'features :', genbank_record.features
	#obtenir un sub record#
	sub_record=get_sub_sequence(genbank_record,10,50)
	print "subrecord : ",sub_record

	#lire un fichier avec de multiples séquences#
	fasta_file_multiple="ls_orchid.fasta"
	record=my_parse_function(fasta_file_multiple,"fasta")

	for rec in record:
		print rec.id
 

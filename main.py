#!/usr/bin/env python
import sys
from seqrecord import *
from seq import *
from seqfeature import *
from entrez import *
from blast import *
if __name__ =="__main__":
	if(sys.argv[1]=="1"):
	#fasta file parsing
		fasta_filename="NC_005816.fna"
		record=my_read_function(fasta_filename, "fasta")
		print '%(GC) : {0}'.format(get_GC_content(record.seq))
		print 'length :', get_len(record.seq)
	#genbank file parsin
	elif (sys.argv[1]== "2"):
		gb_filename="NC_005816.gb"
		genbank_record=my_read_function(gb_filename, "genbank")
		print 'annotation :', genbank_record.annotations["source"]
		for feature in genbank_record.features:
			start,end,strand = get_location(feature)
			if strand == 1:
		 		strand="+"
			else:
		 		strand ="-"
		 	
		print "this feature",feature.type,"start at", start, "and end at",end,"and on strand",strand	
 	#obtenir un sub record
 	elif (sys.argv[1]=="3"):
 		sub_record = get_sub_record(genbank_record,86,1109)
 		print sub_record.seq
 	#lire un fichier avec sequences multiples
 	elif (sys.argv[1]=="4"):
 		fasta_file_multiple="ls_orchid.fasta"
 		record = my_parse_function(fasta_file_multiple,"fasta")
 		for rec in record :
 			print rec.id
 	#Obtenir info bases de donnee NCBI	
 	elif (sys.argv[1]=="5"):
 		result = get_databases()
	 	print result
	 	record = get_database_bis()
	 	print record
	 	record = get_database('pubmed')
	 	print record['DbInfo']['Count']
	 	print record['DbInfo'].keys
 		for field in record['DbInfo']['FieldList']:
 			print field['Name']
 	#mettre bim auteur et initiale pour chercher les articles d'un auteur particulier
 		record = search_database('pubmed','biopython')
 		print record
 		record = fetch_database("nucleotide","8332116")
 		print record
 	#blast
 	elif (sys.argv[1]=="6"):
 		blast_result=get_blast("blastn","nt","8332116")
 		record=read_blast_result(blast_result)

#!/usr/bin/env python

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

def get_blast(blast_type,db_type,blast_id):
	result_handle=NCBIWWW.qblast(blast_type,db_type,blast_id)
	return result_handle

def read_blast_result(blast_result):
	record=NCBIXML.parse(blast_result)
	return record

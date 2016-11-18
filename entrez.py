#!/usr/bin/env python

from Bio import Entrez
from Bio import SeqIO

Entrez.email = "estrella_del_angel@hotmail.com"

def get_databases():
	handle = Entrez.einfo()
	result = handle.read()
	return result
	
def get_database_bis():
	handle = Entrez.einfo()
	record = Entrez.read(handle)
	return record
	
def get_database(db_name):
	handle = Entrez.einfo(db=db_name)
	record = Entrez.read(handle)
	return record
	
def search_database(db_name,term):
	handle=Entrez.esearch(db=db_name,term=term)
	record=Entrez.read(handle)
	return record

def fetch_database(db,id):
	handle=Entrez.efetch(db=db,id=id,rettype="gb",retmode='text')
	record=SeqIO.read(handle,"genbank")
	return record

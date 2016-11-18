#!/usr/bin/env python

from Bio import SeqFeature

def get_location(feature):
	loc=feature.location
	return (loc.start,loc.end,loc.strand)
	#exact_location= feature.FeatureLocation(start,end)
	#return exact_location

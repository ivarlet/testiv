#!/usr/bin/env python

from Bio import SeqFeature

def get_location(feature):
	feature_location = feature.location
	return (feature.location.start,feature.location.end,feature.location.strand)


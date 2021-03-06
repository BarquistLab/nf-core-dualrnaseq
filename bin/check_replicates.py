#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:55:44 2020

@author: B.Mika-Gospodorz


Input file: list of sample names
Output: 'true' or 'false'
Description: Used to identify if there are replicates
"""

import argparse
parser = argparse.ArgumentParser(description="""Are there replicates?""")
parser.add_argument("-s", "--sample_names", metavar='<sample_names>', nargs='+')
args = parser.parse_args()

sample_names = [feature.replace('[' , '').replace(']','').replace(',','') for feature in args.sample_names] #format input file names
suffix_read = [name.rsplit('_', 1)[1] for name in sample_names] #Captures r1, r2 or  R1, R2

#Prints either true or false
#Looking for R1 and R2, or r1 and r2
if ("R1" in suffix_read and "R2" in suffix_read or "r1" in suffix_read and "r2" in suffix_read):
	print('true')
else:
	print('false')


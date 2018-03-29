#!/usr/bin/env python3
#
# n-end_rule.py "single letter amino acid sequence" --organism=["mammalian","scerevisiae","ecoli"]
# This Python script returns the estimated half life of a given protein given the single letter amino acid sequence.
#
# Chris Brumbaugh, cbrumbau@gmail.com, 03/29/2018

import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('protein', action='store', help='Single letter animo acid sequence.')
parser.add_argument('-o', '--organism', choices=['ecoli', 'mammalian', 'scerevisiae'], default='mammalian', help='Type of organism for rules to apply. Default: mammalian')
args = parser.parse_args()

# Half life values provided in
# Tobias, JW, Shrader, TE, Rocap, G & Varshavsky, A (1991). The N-end rule in bacteria. Science, 254, 1374-1377.
# https://doi.org/10.1126%2Fscience.1962196
# Gonda, D K, Bachmair, A, Wünning, I, Tobias, J W, Lane, W S & Varshavsky, A (1989). Universality and structure of the N-end rule.. Journal of Biological Chemistry, 264, 16700-16712.
# http://www.jbc.org/content/264/28/16700.long

# Notes:
# B = Asparagine/Aspartic Acid = N/D
# Z = Glutamine/Glutamic Acid = Q/E

n_end_values = {
	'ecoli' : {
		'A' : '>10 hours',
		'B' : '>10 hours',
		'C' : '>10 hours',
		'D' : '>10 hours',
		'E' : '>10 hours',
		'F' : '~2 minutes',
		'G' : '>10 hours',
		'H' : '>10 hours',
		'I' : '>10 hours',
		'K' : '~2 minutes',
		'L' : '~2 minutes',
		'M' : '>10 hours',
		'N' : '>10 hours',
		'P' : '>10 hours',
		'Q' : '>10 hours',
		'R' : '~2 minutes',
		'S' : '>10 hours',
		'T' : '>10 hours',
		'V' : '>10 hours',
		'W' : '~2 minutes',
		'Y' : '~2 minutes',
		'Z' : '>10 hours'
	},
	'mammalian' : {
		'A' : '4.4 hours',
		'B' : ('1.4 hours','1.1 hours'),
		'C' : '1.2 hours',
		'D' : '1.1 hours',
		'E' : '1 hour',
		'F' : '1.1 hours',
		'G' : '30 hours',
		'H' : '3.5 hours',
		'I' : '20 hours',
		'K' : '1.3 hours',
		'L' : '5.5 hours',
		'M' : '30 hours',
		'N' : '1.4 hours',
		'P' : '>20 hours',
		'Q' : '0.8 hour',
		'R' : '1 hour',
		'S' : '1.9 hours',
		'T' : '7.2 hours',
		'V' : '100 hours',
		'W' : '2.8 hours',
		'Y' : '2.8 hours',
		'Z' : ('0.8 hour','1 hour')
	},
	'scerevisiae' : {
		'A' : '>20 hours',
		'B' : '3 minutes',
		'C' : '>20 hours',
		'D' : '3 minutes',
		'E' : '30 minutes',
		'F' : '3 minutes',
		'G' : '>20 hours',
		'H' : '10 minutes',
		'I' : '30 minutes',
		'K' : '3 minutes',
		'L' : '3 minutes',
		'M' : '>20 hours',
		'N' : '3 minutes',
		'P' : '>20 hours',
		'Q' : '10 minutes',
		'R' : '2 minutes',
		'S' : '>20 hours',
		'T' : '>20 hours',
		'V' : '>20 hours',
		'W' : '3 minutes',
		'Y' : '10 minutes',
		'Z' : ('10 minutes', '30 minutes')
	}
}

# Acquire the N-terminus amino acid
n_terminus_aa = args.protein[:1].upper()
# Report the value
print("The half life value for the protein is ", n_end_values[args.organism][n_terminus_aa], ".", sep="")

sys.exit(0)
#!/usr/bin/env python

from __future__ import division
import sys
import snap
import math 

i = 1
n = 101
p = .1

#edges
e = p* n* (n-1)/2

while(i < 6):
	edgeList = []
	UGraph = snap.GenRndGnm(snap.PUNGraph, n, int(e))
	for EI in UGraph.Edges():
		edgeList.append([EI.GetSrcNId(), EI.GetDstNId()])
	with open("randomgraph.meandegree.10." + str(n) + ".elist.txt", "w") as f:
		for x in edgeList:
			f.write("%d %d\n" % (x[0], x[1]))
	
	n -= 1
	n = (n * 10) + 1
	p = p/10
	i += 1
	

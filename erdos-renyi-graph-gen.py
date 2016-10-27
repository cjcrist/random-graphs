#!/usr/bin/env python

from __future__ import division
import sys
import snap

i = 1
n = 101
p = .1
e = (n-1) * p

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
	
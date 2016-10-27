#!/usr/bin/env python

from __future__ import division
import sys
import snap
import math 

i = 1
n = 101
p = .1
# mean degree - k
k = (n-1) * p
#edges
fact = math.factorial(n) / (math.factorial(k) *math.factorial(n-k))
e = fact * p^(k) * (1-p)^(n-1-k)

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
	

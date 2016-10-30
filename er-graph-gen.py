#!/usr/bin/env python

from __future__ import division
import sys
import os
import snap
import math 

file = sys.argv[1]
filename = file[:-9] + "er" + file[-10:]

inGraph = snap.LoadEdgeList(snap.PUNGraph, file, 0, 1)
nodes = inGraph.GetNodes()
edges = 0

with open(file, "r") as f:
	for x in f:
		edges += 1
print "nodes: %d, edges: %d" % (nodes, edges)

path = os.path.join(r"p3_data", filename[3:])

print "starting ER graph\n"
edgeList = []
UGraph = snap.GenRndGnm(snap.PUNGraph, nodes, edges)
for EI in UGraph.Edges():
	edgeList.append([EI.GetSrcNId(), EI.GetDstNId()])
with open(path, "w") as f:
	for x in edgeList:
		f.write('{0:4d} {1:9d}\n'.format(x[0], x[1]))
print "finished ER graph\n"
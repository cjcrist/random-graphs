#!/usr/bin/env python

from __future__ import division
import sys
import os
import snap
import math 
import time

file = sys.argv[1]
filename = file[:-9] + "ws" + file[-10:]

inGraph = snap.LoadEdgeList(snap.PUNGraph, file, 0, 1)
nodes = inGraph.GetNodes()
edges = 0

with open(file, "r") as f:
	for x in f:
		edges += 1
print "nodes: %d, edges: %d" % (nodes, edges)

path = os.path.join(r"p3_data", filename[3:])

print "starting WS graph at time %s\n" % time.ctime()
edgeList = []
outDegree = 0
OutDegV = snap.TIntPrV()
snap.GetNodeOutDegV(inGraph, OutDegV)
#Sums the value of all out degrees of each node
for item in OutDegV:
    outDegree += item.GetVal2()
    # print "node ID %d: out-degree %d" % (item.GetVal1(), item.GetVal2())
# averages the out degree in OutDeg Vector, and rounds it to the nearest integar
avgOutDegree = round(outDegree/nodes)
# print avgOutDegree

Rnd = snap.TRnd(1,0)
smallWorldGraph = snap.GenSmallWorld(nodes, int(avgOutDegree), 0, Rnd)

for EI in smallWorldGraph.Edges():
	edgeList.append([EI.GetSrcNId(), EI.GetDstNId()])
	with open(path, "w") as f:
		for x in edgeList:
			f.write('{0:4d} {1:9d}\n'.format(x[0], x[1]))

print "finished WS graph at time %s\n" % time.ctime()
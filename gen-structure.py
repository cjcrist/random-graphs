#!/usr/bin/env python

import sys
import snap
import math

# read in file from command line
file = sys.argv[1]

# create a graph
UGraph = snap.LoadEdgeList(snap.PUNGraph, file, 0, 1)
# to view a visual output of the graph data, uncomment
# the line below.
#UGraph.Dump()

# analyzing network
print "\n\t Analyzing Network\n\n"

# 1)  Size of network:
print "Size of the network:\n"
# a) prints the number of nodes in a graph
print "Number of nodes in %s: %d" % (file, UGraph.GetNodes())
# b) print number of edges:
print "Number of edges in %s: %d\n" % (file, UGraph.GetEdges())

# 2) degree of nodes in the network
print "Degree of nodes in the network:\n"
# a) print number of nodes which have degree = 7
Count = snap.CntDegNodes(UGraph, 7)
print "Number of nodes with degree = 7 in %s: %d" % (file, Count)
# b) prints node id(s) for the nodes with the highest degree

maxNodes = []
maxDegree = 0

for node in UGraph.Nodes():
	if (node.GetOutDeg()) > maxDegree:
		maxDegree = (node.GetOutDeg())
		
for node in UGraph.Nodes():
	if (node.GetOutDeg()) == maxDegree:
		maxNodes.append(node.GetId())	
		
print "Node id(s) with the  highest degree in %s: %s\n" % (file, maxNodes)

# c) creates a plot of the out-degree distribution
plotFN = file + ".outDeg.Distribution-plot.png"
snap.PlotOutDegDistr(UGraph, plotFN, "Undirected graph degree distribution for file " + file)
print "\nDegree distribution of %s is in: %s\n" % (file, plotFN)

# 3) Paths in the network:
print "Paths in the network:\n"
# a) approximate full diameter of the graph
# function to calculate the mean
def mean(data):
	return sum(data)/len(data)
# function to calculate the variance
def variance(data):
	n = len(data)
	s = sum(x**2 for x in data) - (sum(data)**2)/n
	return s/(n-1)
	
diam10 = snap.GetBfsFullDiam(UGraph, 10, False)
diam100 = snap.GetBfsFullDiam(UGraph, 100, False)
diam1000 = snap.GetBfsFullDiam(UGraph, 1000, False)

data = [diam10, diam100, diam1000]
m = mean(data)
v = variance(data)

print "Approx. diameter in %s with sampling 10 nodes: %d" % (file, diam10)
print "Approx. diameter in %s with sampling 100 nodes: %d" % (file, diam100)
print "Approx. diameter in %s with sampling 1000 nodes: %d" % (file, diam1000)
print "Approx. diameter in %s (mean and variance): %d, %d\n" % (file, m, v)
# b) approximate effective diameter
effDiam10 = snap.GetBfsEffDiam(UGraph, 10, False)
effDiam100 = snap.GetBfsEffDiam(UGraph, 100, False)
effDiam1000 = snap.GetBfsEffDiam(UGraph, 1000, False)

effData = [effDiam10, effDiam100, effDiam1000]
em = mean(effData)
ev = variance(effData)

print "Approx. effective diameter in %s with sampling 10 nodes: %d" % (file, effDiam10)
print "Approx. effective diameter in %s with sampling 100 nodes: %d" % (file, effDiam100)
print "Approx. effective diameter in %s with sampling 1000 nodes: %d" % (file, effDiam1000)
print "Approx. effective diameter in %s (mean and variance): %d, %d\n" % (file, em, ev)
# c) Plot of the distribution of the shortest path
plotFN1 = file + ".diam.short-path-plot.png"
snap.PlotShortPathDistr(UGraph, plotFN1, "Undirected graph - Shortest path for file " + file)
print "\nShortest path distribution of %s is in: %s\n" % (file, plotFN1)

# 4) Components of the network:
print "Components of the network:\n"
# a) Fraction of nodes in the largest connected component
nodeFrac = snap.GetMxSccSz(UGraph)
print "Fraction of nodes in largest connected component in '%s': %d\n" % (file, nodeFrac)
# b) Plot of the distribution of sizes of connected components.
plotFN2 = file + ".scc.connected-components-plot.png"
snap.PlotSccDistr(UGraph, plotFN2 , "Undirected graph - scc distribution for file " + file)
print "\nComponent size distribution of %s is in: %s\n" % (file, plotFN2)

# end of program
print "\n\t End of program\n\n"
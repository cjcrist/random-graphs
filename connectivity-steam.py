#!/usr/bin/env python
import snap
import sys

#Read in file from command line. 
file = sys.argv[1]


#Create an undirected graph
UGraph = snap.LoadEdgeList(snap.PUNGraph, file, 0, 1)

#Problem 2: Steam Sweden dataset only

print "\n\tProblem 2: Connectivity and Clustering [only for Steam-Sweden dataset]\n"

# 2.1)Number of Triads.
NumTriads = snap.GetTriads(UGraph, -1)
print "2.1)Number of triads: %d\n" %NumTriads

# 2.2) The local clustering coefficient of a randomly selected node. Also report the selected node id.
NI = UGraph.GetRndNId()
NodeClustCf = snap.GetNodeClustCf(UGraph, NI)
print "2.2)Clustering coefficient of random node < %d > in < %s >: %f\n" %(NI, file, NodeClustCf)

# 2.3) Number of triads a randomly selected node participates in. Also report the selected node id.
NI = UGraph.GetRndNId()
NodeTriads = snap.GetNodeTriads(UGraph, NI) 
print "2.3)Number of triads of node < %d > participates in < %d > triads\n" %(NI, NodeTriads)
'''
2.4) The two versions of the global clustering coefficient of the network 
(the average over local clustering coefficients, as in Watts-Strogatz definition, 
and the global clustering coefficient that depends on the number of triangles).
'''
#Watts-Strogatz ClustCoeff
GraphClustCoeff = snap.GetClustCf (UGraph, -1)

#Global ClustCoeff
#Check back
CfVec = snap.TFltPrV()
Cf = snap.GetClustCf(UGraph, CfVec, -1)
print "2.4)Clustering coefficient of the network: < %f > (Watts-Strogatz); < %f > (global)\n" %(GraphClustCoeff, Cf)

# 2.5) Plot of the k-core edge-size distribution: core k vs. number of edges in k-core.
plotN1 = "Steam-Sweden"
snap.PlotKCoreEdges(UGraph, plotN1, "Steam-Sweden Undirected graph - k-core edges")
print "2.5)k-core edge-size distribution is in: < coreEdges.%s.png >\n" %plotN1

# 2.6) Plot of the k-core node-size distribution: core k vs. number of nodes in k-core. 
plotN2 = "Steam-Sweden"
snap.PlotKCoreNodes(UGraph, plotN2, "Steam-Sweden Undirected graph - k-core nodes")
print "2.6)k-core node-size distribution is in: < coreNodes.%s.png >\n" %plotN2

print "\n\tEnd of Problem 2\n"

#!/usr/bin/env python

from __future__ import division
import sys
import os
import snap
import time

# read in file from command line
file = sys.argv[1]
file_name = file[:-9]

path = os.path.join(r"Centrality/imdbActor/ER", file_name)
# create a graph
UGraph = snap.LoadEdgeList(snap.PUNGraph, file, 0, 1)

# analyzing degree centrality
print "\nAnalyzing Degree Centrality at time: " + time.ctime() + "\n"

deg_list = []
# degree centrality
for NI in UGraph.Nodes():
	DegCentr = snap.GetDegreeCentr(UGraph, NI.GetId())
	# prints for testing, but need to output to txt
	deg_list.append([NI.GetId(), DegCentr])
	#print "node: %d centrality: %f" % (NI.GetId(), DegCentr)
# sort list in decending order
deg_list.sort(reverse = True, key=lambda x: x[1])
# iterate through the list and print out each entry
with open(path + "degree.txt", "w") as f:
	f.write("Node ID:\tCentrality:\n")
	for x in deg_list:
		f.write('{0:5d} {1:15.3e}\n'.format(x[0], x[1])) 

# creates plot data with node id replaced by rank
with open(path + "degree.plot.tab", "w") as f:
	f.write("#\n# Plot data for degree centrality\n#\n# rank:\tcentrality:\n")
	i=1
	for x in deg_list:
		f.write('{0:4d} {1:15.3e}\n'.format(i, x[1]))
		i += 1

print "Degree Centrality output to file at time: " + time.ctime() + "\n"

# closeness centrality
print "Analyzing Closeness Centrality at time: " + time.ctime() + "\n"

close_centr_list = []
for NI in UGraph.Nodes():
	CloseCentr = snap.GetClosenessCentr(UGraph, NI.GetId())
	# append the list
	close_centr_list.append([NI.GetId(), CloseCentr])
# sort in decending order
close_centr_list.sort(reverse = True, key=lambda x: x[1])
# iterate through the list and print out each entry
with open(file_name + "closeness.txt", "w") as f:
	f.write("Node ID:\tCentrality:\n")
	for x in close_centr_list:
		f.write('{0:5d} {1:15.3e}\n'.format(x[0], x[1]))

# creates plot data with node id replaced by rank
with open(file_name + "closeness.plot.tab", "w") as f:
	f.write("#\n# Plot data for closeness centrality\n#\n# rank:\tcentrality:\n")
	i=1
	for x in close_centr_list:
		f.write('{0:4d} {1:15.3e}\n'.format(i, x[1]))
		i += 1	

print "Closeness Centrality output to file at time: " + time.ctime() + "\n"

# harmonic closeness centrality
print "Analyzing Harmonic Closeness Centrality at time: " + time.ctime() + "\n"

# this function will calculate the harmonic closeness centrality and place it in a list
harmonicList = []
def harmonic_closeness_centrality():
	sizeGraph = UGraph.GetNodes()
	NIdToDistH = snap.TIntH()

	for node in UGraph.Nodes():
		hashTableCount = 0 
		shortestPath = snap.GetShortPath(UGraph, node.GetId(), NIdToDistH)
		for x in NIdToDistH:
			if (NIdToDistH[x] != 0):	
				hashTableCount += float(1/NIdToDistH[x])
		calculation = float((1/(sizeGraph-1))*hashTableCount)
		harmonicList.append([node.GetId(), calculation])

	return harmonicList 

harmonic_closeness_centrality()
# sorts the list of harmonic closeness centrality in decending order
harmonicList.sort(reverse = True, key=lambda x: x[1])

# creates a new txt file and writes to file the content of the list
with open(file_name + "harmonic.txt", "w") as f:
	f.write("Node ID:\tCentrality:\n")
	for x in harmonicList:
		f.write('{0:5d} {1:15.3e}\n'.format(x[0], x[1]))

# creates plot data with node id replaced by rank
with open(file_name + "harmonic.plot.tab", "w") as f:
	f.write("#\n# Plot data for harmonic closeness centrality\n#\n# rank:\tcentrality:\n")
	i=1
	for x in harmonicList:
		f.write('{0:4d} {1:15.3e}\n'.format(i, x[1]))
		i += 1

print "Harmonic Closeness Centrality output to file at time: " + time.ctime() + "\n"

# betweenness centrality
print "Analyzing Betweenness Centrality at time: " + time.ctime() + "\n"

Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
nodeFrac = 1.0
between_centr = snap.GetBetweennessCentr(UGraph, Nodes, nodeFrac)
between_node_list = []
# still needs to sort by decending centrality and write to text
for node in Nodes:
	#print "nodes: %d centrality: %f" % (nodes, Nodes[nodes])
	between_node_list.append([node, Nodes[node]])

# sort the list in decending order
between_node_list.sort(reverse = True, key=lambda x: x[1])

# write node id and betweenness centrality to file
with open(file_name + "betweenness.txt", "w") as f:
	f.write("Node ID:\tCentrality:\n")
	for x in between_node_list:
		f.write('{0:5d} {1:15.3e}\n'.format(x[0], x[1]))

# creates plot data with node id replaced by rank
with open(file_name + "betweenness.plot.tab", "w") as f:
	f.write("#\n# Plot data for betweenness centrality\n#\n# rank:\tcentrality:\n")
	i=1
	for x in between_node_list:
		f.write('{0:4d} {1:15.3e}\n'.format(i, x[1]))
		i += 1

print "Betweenness Closeness Centrality output to file at time: " + time.ctime() + "\n"

# Local Clustering Coefficient
print "Analyzing Local Clustering Coefficient at time: " + time.ctime() + "\n"

# Computes clustering coefficient of each node in the network
localClusterCoeffList = []
for node in UGraph.Nodes():
	localNodeClustCoeff = snap.GetNodeClustCf(UGraph, node.GetId())
	localClusterCoeffList.append([node.GetId(), localNodeClustCoeff])

# sort the list of local node clustering coefficient
localClusterCoeffList.sort(reverse = True, key=lambda x: x[1])

# write the list of node ids and local clustering coefficients to file
with open(file_name + "clustering.txt", "w") as f:
	f.write("Node ID:\tLocal Clustering Coefficient:\n")
	for x in localClusterCoeffList:
		f.write('{0:5d} {1:15.3e}\n'.format(x[0], x[1]))

# creates plot data with node id replaced by rank
with open(file_name + "clustering.plot.tab", "w") as f:
	f.write("#\n# Plot data for local clustering coefficient\n#\n# rank:\tlocal clustering coeffiecient:\n")
	i=1
	for x in localClusterCoeffList:
		f.write('{0:4d} {1:15.3e}\n'.format(i, x[1]))
		i += 1

print "Local Clustering Coefficient output to file at time: " + time.ctime() + "\n"

print "\n\t\t\tEnd of Problem 1\n"
import sys
sys.path.append('../')

import networkx as nx
import boolparser
import gprops
import subgraph

#the brackets have to be {} and not () for the file to be read.
rulefile = 'dauer_rules.txt'
G = boolparser.readfile(rulefile)
gprops.set_edge_type(G)
print(G.nodes()) 

gfile = 'C:/Users/Alekhya Abhiram/ML_course/PH482_582/suff_necc/examples/dauer_model2.graphml'
nx.write_graphml(G,gfile)
#nx.draw(G)
#plt.show()

print ('Graph created at', gfile)

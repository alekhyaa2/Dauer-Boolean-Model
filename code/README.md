# 1. Simulations

File: simulation.ipynb 
Scripts: Boolean2 
         https://github.com/ialbert/booleannet.git

Notes: simulate the system under favourable (cmk-1=1, pher=0) and unfavourable (cmk-1=0, pher=1) conditions using asynchronous update. Perform perturbation experiments to emulate daf-c and daf-d mutants. Plot graphs using seaborn to look at the simulation trajectories in different simulation settings. 


## **2. Stable motif Analysis**

File: dauer_stable motifs.ipynb
Scripts: pystablemotifs
         https://github.com/jcrozum/pystablemotifs.git

Notes: Extract attractors and stable motifs. Identify driver nodes for a specific target to control the attarctors. 


## **3. Logic backbone**

File: network_red.ipynb
Scripts: https://github.com/parulm/suff_necc.git

Notes: Perform logic based reduction of the model using the functions LVC, edge_red, and node_collapse. Identify stable motifs using subgraphs and verify from what we observe in previous stable motif analysis. Extract subgraphs from signals to motif nodes and subgraphs from motif nodes to motif nodes and finally subgraphs fro mmotif nodes to output node to build the logic backbone.  
## Scripts

print_states.ipynb -> Running simulations for systems exhibits wild type and daf-c/daf-d mutant phenotypes. 
                      Saving states of each node in stead state of teh system in every simulation. 
                      
dauer_stable motifs.ipynb -> Identify the attractors, stable motifs, and driver nodes of the dauer network. 

# 1. Simulations

File: simulation.ipynb\
Scripts: Boolean2 
         https://github.com/ialbert/booleannet.git

Notes: simulate the system under favourable (cmk-1=1, pher=0) and unfavourable (cmk-1=0, pher=1) conditions using asynchronous update. Perform perturbation experiments to emulate daf-c and daf-d mutants. Plot graphs using seaborn to look at the simulation trajectories in different simulation settings. 


# 2. Stable motif Analysis

File: dauer_stable motifs.ipynb\
Scripts: pystablemotifs
         https://github.com/jcrozum/pystablemotifs.git

Notes: Extract attractors and stable motifs. Identify driver nodes for a specific target to control the attarctors. 


# 3. Logic backbone

File: network_red.ipynb\
Scripts: https://github.com/parulm/suff_necc.git

Notes: Useful to convert text file to graphml file. 


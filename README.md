# HPC-Twitter-Processing-paralleling
## This is a program assignment of Cluster and Cloud Computing of semester 1 in 2020
### the program is to implement a simple, parralledlized application leveraging the University of Melbourne HPC facility SPARTAN
### The last test on HPC  will use a large Twitter dataset for Sydney.
### Before that, small and tiny Twitter dataset were tested locally.  

#### composition of program  
    1. [Assignment1-code.py](https://github.com/CinderCC/HPC-Twitter-Processing-paralleling/blob/master/Assignment1-code.py)    
       is the main part to operate the program by using paralleling.
    2. the Slurm files are to control and allow the given number of nodes and cores to be utilized in the searching.   
       + 1 node and 1 core
       + 1 node and 8 cores
       + 2 nodes adn 8 cores (4 cores per node)  
 
#### The solution of searching is to identify the top 10 most commonly used hashtags and languages and the number of times they appear.

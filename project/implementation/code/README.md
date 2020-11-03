# README for the code

 * **main.py** -- use this to run the force directed graph algorithm on a graph. 
 The only command line arg is the file path containing the input graph. 
 The output (written to a directory with the same name as the input file) consists of a bunch of graph files that have the vertices, positions, and edges.
 * **make-gif.py** -- use this to make a gif based on a bunch of graph files.
 The command line arguments are the directory containing the graph files and a step size for which graph files to process (should be a number).
 * **\*.py** -- these other files are used by main and make-fig at various times.
 * **generators/** -- a directory containing some scripts that will generate initial graph files.

(I had trouble getting nltk modules to download on my laptop so I used Docker to generate an environment to run in.)

See below for commands -- `Makefile` and `Dockerfile` define my workflow.

The primary entry point is `jkent-challenge.py`, and my modules are `file_tokens.py`, `pos_histo.py`, and `trigram_chart.py`

Output files are, as specified in the doc file, `Trigrams.csv` and `Speech.jpg`

(with docker and make installed)  
`make build`  
`make run`  
  
(if you have vscode installed)  
`make show`  

(cleanup)  
`make clean`  
`make rebuild`  
  
(without docker installed, but with nltk and matplotlib)  
`python3 jkent-challenge.py`  

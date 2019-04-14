#! /bin/bash

rm -rf pagerank_out/

#python pagerank_simplified.py -r local soc-Epinions1.txt --output-dir=pagerank_out --no-output

#python file.py -r local soc-Epinions1.txt --output-dir=pagerank_out --no-output

#python encode.py -r local soc-Epinions1.txt --output-dir=pagerank_out --no-output

#python sample.py -r local soc-Epinions1.txt --output-dir=pagerank_out --no-output

python pagerank.py -r local soc-Epinions1.txt --output-dir=pagerank_out --no-output
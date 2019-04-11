#! /bin/bash

# Cleansup previous output folder
rm -rf word_count_out/

#python pairs.py -r local samplejokes.csv --output-dir=word_count_out --no-output

#python word_count_pairs.py -r local samplejokes.csv --output-dir=word_count_out --no-output

python word_count_pairs.py -r local shortjokes.csv --output-dir=word_count_out --no-output

#python test_pairs.py -r local samplejokes.csv --output-dir=word_count_out --no-output

#python word_count_stripes.py -r local samplejokes.csv --output-dir=word_count_out --no-output

#python word_count_stripes.py -r local shortjokes.csv --output-dir=word_count_out --no-output

#python stripes.py -r local shortjokes.csv --output-dir=word_count_out --no-output
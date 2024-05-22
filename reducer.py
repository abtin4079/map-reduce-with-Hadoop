#!/usr/bin/env python
"""reducer.py - Processes key-value pairs received from the mapper, where each key is a word 
and each value is a document ID where the word appeared. This script aggregates the document IDs 
for each word and outputs the word alongside the set of unique document IDs where the word was found.
The reducer reads lines of input from standard input, where each line has a format of 'word,document_id'.
The input lines are expected to be sorted by the word. The reducer uses this sorted order to efficiently
aggregate document IDs by using a set data structure, transitioning between different words as it processes
the input lines one-by-one.
"""
import sys 

current_word = None
index = set()

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t')

    if current_word and current_word != word:
        print(f"{current_word} {{{', '.join(index)}}}")
        index = set()

    current_word = word
    index.add(count)

if current_word:
    print(f"{current_word} {{{', '.join(index)}}}")
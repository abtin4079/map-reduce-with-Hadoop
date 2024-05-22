#!/usr/bin/env python3
import sys
from collections import defaultdict, Counter

# Number of top words to output
k = 3
# Dictionary to hold the word counts per document
word_counts = defaultdict(Counter)

# Process each line from the input
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    word, doc_id, count = line.split('\t')
    count = int(count)
    word_counts[doc_id][word] += count

# Output the top k words for each document
for doc_id, counter in word_counts.items():
    most_common_words = counter.most_common(k)
    for word, count in most_common_words:
        print(f"{doc_id},{word},{count}")

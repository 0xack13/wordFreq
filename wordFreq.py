from collections import Counter

# Load the file and extract the words
lines = open("gettysburg-address.txt").readlines()
words = [ w for l in lines for w in l.rstrip().split() ]
print 'Words in text:', len(words)

# Use counter to get the counts
counts = Counter( words )

# Sort the (word, count) tuples by the count, then the word itself,
# and output the k most frequent
k = 4
print 'Frequent words:'
for w, c in sorted(counts.most_common(k), key=lambda (w, c): (c, w), reverse=True):
    print '%s %s' % (w, c)
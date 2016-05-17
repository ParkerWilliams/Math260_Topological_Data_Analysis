import numpy as np
import math
import sys

#no error handling, for shame

infile = sys.argv[1]
outfile = sys.argv[2]


data = np.load(str(infile))

def k_subsets_i(n, k):
    '''
    Yield each subset of size k from the set of intergers 0 .. n - 1
    n -- an integer > 0
    k -- an integer > 0
    '''
    # Validate args
    if n < 0:
        raise ValueError('n must be > 0, got n=%d' % n)
    if k < 0:
        raise ValueError('k must be > 0, got k=%d' % k)
    # check base cases
    if k == 0 or n < k:
        yield set()
    elif n == k:
        yield set(range(n))

    else:
        # Use recursive formula based on binomial coeffecients:
        # choose(n, k) = choose(n - 1, k - 1) + choose(n - 1, k)
        for s in k_subsets_i(n - 1, k - 1):
            s.add(n - 1)
            yield s
        for s in k_subsets_i(n - 1, k):
            yield s

output = []

for x in range(0,len(data)):
    distances = []
    for y in range (0,len(data)):
        if (data[x] != data[y]).all():
            d = math.sqrt((data[x][0]-data[y][0])**2+(data[x][1]-data[y][1])**2+(data[x][2]-data[y][2])**2)
            distances.append(d)
    vert = list(data[x])
    vert.append(min(distances))
    output.append(vert)


f = open(str(outfile), 'w')
f.write('3\n1 .01 1000\n')
for l in output:
    outline = (" ".join( repr(e) for e in l ) + '\n')
    f.write(outline.replace('\'',""))
f.close()

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

for x in k_subsets_i(len(data),3):
    first = list(x)[0]
    second = list(x)[1]
    third = list(x)[2]
    d1 = math.sqrt((data[first][0]-data[second][0])**2+(data[first][1]-data[second][1])**2+(data[first][2]-data[second][2])**2)
    d2 = math.sqrt((data[first][0] - data[third][0]) ** 2 + (data[first][1] - data[third][1]) ** 2 + (data[first][2] - data[third][2]) ** 2)
    d3 = math.sqrt((data[second][0] - data[third][0]) ** 2 + (data[second][1] - data[third][1]) ** 2 + (data[second][2] - data[third][2]) ** 2)
    birthTime = max(d1,d2,d3)
    output.append([", ".join(map(str,list(data[first]))),", ".join(map(str,list(data[second]))),", ".join(map(str,list(data[third]))),birthTime])
    print(list(x))

f = open(str(outfile), 'w')
f.write('2\n3\n')
for l in output:
    outline = (", ".join( repr(e) for e in l ) + '\n')
    f.write(outline.replace('\'',""))
f.close()

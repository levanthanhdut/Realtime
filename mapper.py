#!/usr/bin/env python
import sys
import time

#--- get all lines from stdin ---
start_time = time.time()
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    words = line.split()

    
    #--- output tuples [word, 1] in tab-delimited format---
    for word in words: 
        print ('%s\t%s' % (word, "1"))
    if line=="x": break
end_time=time.time()
print ('total run-time: %f s' % (end_time - start_time))

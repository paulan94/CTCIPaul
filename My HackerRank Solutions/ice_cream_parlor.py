#Paul An
'''Each time Sunny and Johnny take a trip to the Ice Cream Parlor, 
they pool together  dollars for ice cream. On any given day, the parlor offers a line of  flavors. 
Each flavor, , is numbered sequentially with a unique ID number from  to  and has a cost, , associated with it.'''
t = int(raw_input().strip())


def print_indexes(m, n, a):
    john = 0;
    for i in range(n - 1):
        john = i + 1
        counter = 0
        while (john < n or counter > 100):
            if a[i] + a[john] == m:
                print i + 1, john + 1
                break
            else:
                john += 1
                continue
            counter += 1


for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    print_indexes(m, n, a)
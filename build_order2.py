##def build_order(processes):
##    temp = set()
##    perm = set()
##    res = []
##    for i in range(len(processes)):
##        if i not in perm:
##            visit(i, processes,temp,perm,res)
##
##    return res
##
##
##def visit(process, processes, temp, perm, res):
##    if process in temp:
##        raise Exception("oopsie")
##    if not process in perm:
##        temp.add(process)
##        for i in processes[process]:
##            visit(i,processes,temp,perm,res)
##
##        perm.add(process)
##        temp.remove(process)
##        res.append(process)

def build_order(processes):
    temp = set()
    perm = set()
    res = []
    for i in (list(processes.keys())[::-1]):
        if i not in perm:
            visit(i, processes,temp,perm,res)

    return res


def visit(process, processes, temp, perm, res):
    if process in temp:
        raise Exception("oopsie")
    if not process in perm:
        temp.add(process)
        for i in processes[process]:
            visit(i,processes,temp,perm,res)

        perm.add(process)
        temp.remove(process)
        res.append(process)

##x = {0: [],
##     1: [0],
##     2: [0],
##     3: [1,2],
##     4: [3]
##     }

p= ['a','b','c','d','e', 'f']
d = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]


def graphify(p,d):
    graph = dict()
    for proj in p:
        graph[proj] = []
    for dep in d:
        graph[dep[1]].append(dep[0])
    return graph

graph = (graphify(p,d))
##x2 = [
##    ['f'],
##    ['f'],
##    ['d'],
##    ['a','b'],
##    []] #a,b,c,d,e

print (build_order(graph))



def build_order(processes):
    temp = set()
    perm = set()

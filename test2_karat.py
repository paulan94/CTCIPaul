inp = [
    ['58', 'SWE'],
    ['58', 'LINAlG'],
    ['94', 'ART'],
    ['17', 'SWE'],
    ['94', 'SWE'],
    ['66', 'ART']
    ]
##('94', '58') ['S', 'W', 'E']
##('58', '17') ['S', 'W', 'E']
##('94', '17') ['S', 'W', 'E']
##('66', '17') []
##('66', '58') []
##('94', '66') ['A', 'R', 'T']
from collections import defaultdict


def find_shared_courses(sid_course):
    SIDS = set()
    course_dict = defaultdict(list)
    for x in sid_course:
        SIDS.add(x[0])
        course_dict[x[1]].append(x[0])
    SIDS = list(SIDS)
    pair_dict = create_pair_dict(SIDS)
    print (course_dict.items())

    for k,v in course_dict.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                if v[i] > v[j]:
                    bigger = v[i]
                    smaller = v[j]
                else:
                    bigger = v[j]
                    smaller = v[i]
                pair_dict[(bigger,smaller)] = k
    return pair_dict
        


def create_pair_dict(SIDS):
    pd = dict()
    for i in range(len(SIDS)):
        for j in range(i+1, len(SIDS)):
            if int(SIDS[i]) > int(SIDS[j]):
                bigger = SIDS[i]
                smaller = SIDS[j]
            else:
                bigger = SIDS[j]
                smaller = SIDS[i]
            pd[(bigger,smaller)] = []
    return pd

x = find_shared_courses(inp)

for k,v in x.items():
    print (k,v)

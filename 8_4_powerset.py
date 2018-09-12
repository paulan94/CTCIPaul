s = set()
s.add(1)
s.add(2)
s.add(3)
print (s)

def power_set(some_set):
    arr = []
    if len(some_set) >= 0:
        arr.append([])
        for idx in range(len(some_set)):
            arr.append(list(some_set)[idx])
            for jdx in range(idx+1, len(some_set)):
                arr.append(list(some_set)[idx:jdx+1])

    return arr

print (power_set(s))

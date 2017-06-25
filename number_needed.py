
def number_needed(a, b):
    dict_a = dict()
    dict_b = dict()
    num_del = 0
    for i in a:
        if i in dict_a:
            dict_a[i] += 1
        else:
            dict_a[i] = 1
    for j in b:
        if j in dict_b:
            dict_b[j] += 1
        else:
            dict_b[j] = 1
    for i,k in dict_a.items():
        if i not in dict_b.keys():
            num_del += k
        #this case has to be handled just once. if i exists in dictb, we need to add the abs value of (dict_a[i]) - dict_b[i].
        if i in dict_b.keys(): 
            num_del += abs(k-dict_b[i])
    for i,k in dict_b.items():
        if i not in dict_a.keys():
            num_del += k
    return num_del

a = "abcdbc"
b = "cde"

print (number_needed(a, b))

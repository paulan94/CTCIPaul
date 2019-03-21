

def magic_string(n, comb = ['a','e','i']):
    c = 0
    while c < n:
        new_comb = []
        for ele in comb:
            if ele[-1] == 'a':
                new_comb.append(ele + 'e')
            elif ele[-1] == 'e':
                new_comb.append(ele + 'a')
                new_comb.append(ele + 'i')
            elif ele[-1] == 'i':
                new_comb.append(ele + 'a')
                new_comb.append(ele + 'e')
                new_comb.append(ele + 'i')
        
        c += 1
        if c == n:
            return len(comb)
        comb = new_comb
        



print (magic_string(3))


                 

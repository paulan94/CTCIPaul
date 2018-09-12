
def get_parens(n):
    if n == 0: return ['']
    else:
        p_list = []
        parens = get_parens(n-1)
        for each in parens:
            p_list.append('()' + each)
            p_list.append('(' + each + ')')
            p_list.append(each + '()')
        return set(p_list)

print (get_parens(4))
print (get_parens(3))
print (get_parens(2))
print (get_parens(1))
print (get_parens(0))

pd = {'{': '}',
          '[': ']',
          '(': ')'}
closed = '}])'

def valid_equation(S):
    stck = []
    for c in S:
        if c in pd.keys():
            stck.append(pd[c])
        elif c in closed:
            if c != stck.pop():
                return False
    return len(stck) == 0

print (valid_equation('{3*[1+5(6+8)]}')) #T
print (valid_equation('{3*[1+5(6+8])}')) #F
print (valid_equation('{3*[1+5(6+8)]')) #F
            
            
    

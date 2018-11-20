# 8 x 6

def mult(x,y):
    print (x,y)
    if y == 0: return 0
    elif y == 1: return x

    else:
        smaller = y >> 1
        half = mult(x,smaller)
        if y % 2 == 0:
            return half + half
        else:
            return half + half + x

print (mult(8,6))
        
        
        

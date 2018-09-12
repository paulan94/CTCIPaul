
def str_rotate(str1,str2):
    if str1 == str2:
        return True
    else:
        idx = len(str1)
        while idx >= 0:
            if str1[:idx] in str2:
                x = str1[:idx]
                y = str1[idx:]
                print (x, y)
                print (y,x)
                return (x+y == str1) and (y+x == str2)
            idx -= 1
        return None

print (str_rotate("waterbottle", "erbottlewat"))

def revString(somestring):
    strlen = len(somestring)
    ans_string = ""
    index = strlen
    print (index)
    while (index > 0):
        ans_string += somestring[index-1]
        print (ans_string)
        index -= 1
    return ans_string

print (revString("hello"))
        

# Complete the function below.
# () -> ()
# ba)r) -> bar
# b(a)r) -> b(a)r, OR b(ar)
# )( -> ""
# ((((( -> ""
# (()()( ->  ()(), (())

# (())(
# open: 3
# close: 2
# (())###

# count += 1 ")"
# count -= 1 "("
# count += 1
# count -= 1 #

#given string with alphanumeric chars and parentheses. Goal is to return string
#with balanced parentheses by removing the fewest characters possible.

##'dfe23' # -> dfe23

#)( -> ""
# b(a))(r -> b(a)
# ()()))( -> ()()
# (()))(() -> (())()

# ()())((

def balance_parens(some_str):
    count = 0
    #list so i can mutate it. strings are immutable
    str_list = list(some_str)
    #this part removes all unnecessary closing parens
    for idx,c in enumerate(some_str):
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1
            if (count < 0):
                str_list[idx] = "#"
                count = 0
##    print (str_list)
    #use same logic in reversed string list to remove  unnecessary opening
    str_list2 = (str_list[::-1])
    count = 0
    for idx, c in enumerate(some_str[::-1]): #idx is reverse though
        if c == ")":
            count += 1
        elif c == "(":
            count -= 1
            if (count < 0):
##                str_list2[len(str_list2)-1-idx] = "#"
                str_list2[idx] = "#"
                count = 0
    result = ""
    str_list2 = str_list2[::-1]
    for char in str_list2:
        if (char != "#"):
            result += char
    return result

print (balance_parens('())))()')) #need to remove # after
print (balance_parens('(()(()('))
print (balance_parens('()'))
print (balance_parens('ba)r'))
print (balance_parens(')('))
# ba)r) -> bar
# b(a)r) -> b(a)r, OR b(ar)
# )( -> ""
# ((((( -> ""
# (()()( ->  ()(), (())
        

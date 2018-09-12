# Enter your code here. Read input from STDIN. Print output to STDOUT
# Your given list of integers

# [1,2,2,1]
# + * ( )

# 1+ 2 + 2 + 1 = 6

# 1 * 2 * 2 * 1 = 4

# (1*2) + (2*1) = 4



# [2,2,1,2]
# 2+2+1+2 = 7
# (2*2) + (1+2) = 7

# ((2*2) + 1) * 2 = 10
# 2 * (2+1) * 2 = 12

# Goal: Return greatest number OR the equation of the greatest number

#get all possible permutations of int elements with equations
#base case and build
#if len(arr) > 2: insert parens where we can
#["1+", "1*", 1+2, 1*2, 1+2*2, 1+2+2, (1+2)*2, (1+2)+2, 1+(2*2), 1+(2+2)]
#we know ints are going to be in order
#get list of equations and call eval() to get equation value.

def find_perm(int_arr): #return int representing max from equation
    perm_set = []
    if len(int_arr) == 1:
        return int_arr
    else:
        first_int = int_arr[0]
        remainder = int_arr[1:]
        ints = find_perm(remainder)
        for i in ints:
            perm_set.append(str(first_int) + "+" + str(i) )
            perm_set.append(str(first_int) + "*" + str(i) )
        return perm_set
        
def add_parens(arr):
    new_arr = []
    for expr in arr:
        for idx in range(len(expr)):
            for jdx in range(idx+1, len(arr)):
                new_arr.append(("(" + str(expr[idx: jdx]) + ")" + str(expr[jdx:])))
    return new_arr
    
def eval_highest(some_set):
    high = 0
    highest_expr = ""
    for expr in some_set:
        try:
            if eval(expr) > high:
                high = eval(expr)
                highest_expr = expr
        except:
            pass
    print ("highest val: {} \nHighest val expression: {}".format(high, highest_expr))
            
    
perms_no_parens = find_perm([1,2,2,1])
perms_with_parens = add_parens(perms_no_parens)
eval_highest(perms_with_parens)

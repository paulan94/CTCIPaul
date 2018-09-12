def get_parens(arr, num_left,num_right, S, idx):
    if (num_left < 0 or num_right < num_left):
        return

    if (num_left == 0 and num_right == 0):
        print (S)
        arr.append("".join(x for x in S))

    else:
        S[idx] = '('
        print ("idx 1: ", idx)
        get_parens(arr,num_left-1,num_right,S,idx+1)

        S[idx] = ')'
        print ("idx 2: ", idx)
        get_parens(arr,num_left,num_right-1,S,idx+1)
    


def gen_parens(n):
    S = [n] * n*2
    arr = []
    get_parens(arr,n,n,S,0)
    return arr

x = gen_parens(3)

print (x)

##def get_parens(n):
##    st = set()
##    if n == 0:
##        st.add("")
##    else:
##        rem = get_parens(n-1)
##        for each in rem:
##            st.add('(' + each + ')')
##            st.add('()' + each)
##            st.add(each + '()')
##    return st
##
##print (get_parens(3))

def solution(N):
    # write your code in Python 3.6
    #assuming N < 10000
    str_list = list(str(N))
    str_list.sort(reverse = True)
    return int(''.join(x for x in str_list))


for i in range(10001):
    print (solution(i))

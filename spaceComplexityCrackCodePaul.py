#Paul An
def pairSumSeq(n):
    ans_sum = 0;
    for i in range(n):
        ans_sum += pairSum(i,i+1)
    return ans_sum

def pairSum(a, b):
    return a+b

if __name__ == "__main__":
    print (pairSumSeq(2))

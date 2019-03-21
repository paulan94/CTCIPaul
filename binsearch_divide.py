
#binsearch_divide(31,5) -> q: 6, r: 1
def binsearch_divide(numerator,divisor):
    start = 0
    end = numerator
    mid = numerator >> 1    #bitshift operator to divide by 2

    remainder = numerator - (mid * divisor)

    while not (remainder >= 0 and remainder < divisor):
        if remainder < 0:
            end = mid
        else:
            start = mid

        mid = end + start >> 1
        remainder = numerator - (mid * divisor)

    print ("quotient: {} remainder: {}".format(mid,remainder))
            

binsearch_divide(31,5)    

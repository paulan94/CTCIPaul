import random

#Paul An Look/Leap Problem 

def look(numList):
    #look at random 37% of list, then return best
    max_num = 0
    for i in range(int(len(numList)*0.37)):
        if numList[i] > max_num:
            max_num = numList[i]
    return max_num

def leap(max_num, numList):

    for i in numList:
        if i > max_num:
            return i
    return i


def main():
    avg = 0.0
    num_tests = 100
    for i in range(num_tests):
        counter = 0
        for i in range(100):
            numList = []
            for i in range(100):
                num = random.randint(1,100)
                if num not in numList:
                    numList.append(num)
            lk = look(numList)
            lp = leap(lk,numList)
            if lp == max(numList): #if the leap was the max num in numList
##                print lp #uncomment if you want to see the max num
                counter += 1
        avg += counter
    ##    print '\:{}'.format(counter) #UNCOMMENT if want to see counter for each instance
    avg /= num_tests
    print avg
    
if __name__ == "__main__":
    main()

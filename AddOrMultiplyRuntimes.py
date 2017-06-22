def addRunTimeAlgorithm(arrayA, arrayB):
    #   O(A+B)
    for a in arrayA:
        print (a)
    for b in arrayB:
        print (b)

def multiplyRunTimeAlgorithm(arrayA, arrayB):
    #   O(AB)
    for a in arrayA:
        for b in arrayB:
            print (str(a) + "," + str(b))

if __name__ == "__main__":
    arrayA = ["a","b","c"]
    arrayB = [1,2,3,4]
    print ("Running add runtimes function!")
    addRunTimeAlgorithm(arrayA, arrayB)
    print ("End add runtimes function\nStarting multiply runtimes function!")
    multiplyRunTimeAlgorithm(arrayA, arrayB)
    print ("End multiply runtimes function!")

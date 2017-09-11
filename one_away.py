#Paul An
#CTCI 1.5 One Away 

def main(word1, word2):
    if len(word1) > len(word2):
        for char_index in range(len(word1)):
            #handle if char_index > len(word2)
            if char_index == len(word2):
                word1 = word1[:char_index]
            elif (word1[char_index] != word2[char_index]):
                word1 = word1[char_index:]
            print word1, word2
            
    
    return True

if __name__ == "__main__":
     print (main('pale', 'ale'))

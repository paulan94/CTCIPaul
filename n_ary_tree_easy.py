# Enter your code here. Read input from STDIN. Print output to STDOUT

#                                 CEO
#                     VP          VP          VP
#                 D D  D      D   D  D      D   D  D


# Maximize fun at the party 

#                                   10
#                      100         -10        100
#                   1 2  2         3 3 3     2  2  2

// # 209 ---> 209 harder version

// # 200 -> easier version


#                                   10
#                      0             0         0
#                   1 2  2         3 3 3     2  2  2

# 10 + 5 + 9 + 6 = 30  in the easier version

# approach: sum up values in each level of the tree, add with nodes in level + 2, and compare total against nodes in  level + 1 + level +3

#                                   10                      lvl1 = 10, lvl2 = 190, lvl3 = 20
#                      100         -10        100           lvl1 + lvl 3 = 30
#                   1 2  2         3 3 3     2  2  2        max(190, 30) = 190


#                                   10                      lvl1 = 10, lvl2 = 190, lvl3 = 317, lvl4 = 14
#                      100         -10        100           lvl1 + lvl 3 = 317
#                   1 2  2         3 300 3   2  2  2        lvl2 + lvl4 = 204
#                   1 1 2 4       5 2 2  2                  max(317,204) = 317

def get_max_fun(root):
    odd_level_total, even_level_total = 0,0
    queue = Queue()
    if not root: return None
    else:
        level = 1
        queue.enqueue(root)
        while not queue.isEmpty():
            node = queue.dequeue()
            level_sum = 0
            level += 1 #keep track of levels
            for adj_node in node.adjacent:
                level_sum += adj_node.fun_value
            if level % 2 == 1:
                odd_level_total += level_sum
            else:
                even_level_total += level_sum
        
        return max(odd_level_total, even_level_total)


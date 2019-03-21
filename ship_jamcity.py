# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

ORD_SUB = 64
def solution(N, S, T):
    # write your code in Python 3.6
    
    #ship stuff
    total_sunken = 0
    total_hit_not_sunken = 0

    ship_list = create_ship_list(S)
    hit_list = create_hit_list(T)
    
    for ship in ship_list:
        #for each ship, check if the hit matches a coord on the ship
        for hit_x,hit_y in hit_list:
            ship.hit_ship(hit_x,hit_y)
            
    for ship in ship_list:
        if ship.is_sunken:
            total_sunken += 1
        elif ship.is_hit:
            total_hit_not_sunken +=1
    
    return str(total_sunken) + ',' + str(total_hit_not_sunken)

def create_hit_list(hits):
    hit_list = []
    for t in hits.split(' '):
        for c in t:
            if c.isalpha():
                x = int(t[:t.index(c)])
                y = ord(t[t.index(c)]) - ORD_SUB
                hit_list.append((x,y))
    return hit_list

def create_ship_list(S):
    ship_list = []
    for ship_coords in S.split(','):
        ship_coords = ship_coords.split(' ')
        top_left = ship_coords[0]
        bottom_right = ship_coords[1]
        for c in top_left:
            if c.isalpha():
                top = int(top_left[:top_left.index(c)])
                left = ord(top_left[top_left.index(c)]) - ORD_SUB
        for c in bottom_right:
            if c.isalpha():
                bottom = int(bottom_right[:bottom_right.index(c)])
                right = ord(bottom_right[bottom_right.index(c)]) - ORD_SUB
                
        #add ship class
        ship_list.append(Ship(top,left,bottom,right))
    
    return ship_list

class Ship():
    def __init__(self, top, left, bottom, right):
        
        self.coords = [] # list
        self.coords_hit = []
        self.is_hit = False
        self.is_sunken = False
        for i in range(top,bottom+1):
            for j in range(left,right+1):
                self.coords.append((i,j))
    def hit_ship(self, x,y):
        if (x,y) in self.coords:
            self.is_hit = True
            self.coords_hit.append((x,y))
        if len(self.coords) == len(self.coords_hit):
            self.is_sunken = True
        

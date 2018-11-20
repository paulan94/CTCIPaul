class ASCII_Printer():
    def __init__(self, size, command_stream):
        self.board = [[LL()]*size for _ in range(size)]

    def draw_rect(self,char,x_s,y_s,x_e,y_e):
        #assuming x,y in bounds
        new_node = Node(char)

        #not sure why its filling out!!
        for row in range(x_s, x_e+1):
            for col in range(y_s,y_e+1):
                self.board[row][col].add_new(new_node)

    def print_canvas(self):
        board_copy = self.board[:] #make shallow copy
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if not self.board[col][row].head:
                    board_copy[col][row] = ' '
                else:
                    board_copy[col][row] = self.board[col][row].head.val
        for row in board_copy:
            print (row)

    def bring_rect_front(self,x,y):
        LL_cell_val = self.board[x][y].head.val
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.check_cell_has_val(LL_cell_val,x,y):
                    #some sort of caching.
                    self.delete_then_add(self.board[row][col], LL_cell_val)
        
        
        #go through board, check if the cells value is the same as our cell at
        #x,y, if so, bring that cell to the front
        return

    def drag_rect(self,start_x, start_y, end_x, end_y):
        #get head cell of LL, and move rectangle to end_x, end_y
        return
    


class LL():
    def __init__(self,head=None):
        self.head = head
        
    def add_new(self,node):
        node.next = self.head
        self.head = node
            
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
        
        
        
        
size = 6
ap = ASCII_Printer(size,"")
ap.draw_rect('L',1,1,4,4)
ap.draw_rect('R', 2,1,4,4)
ap.print_canvas()

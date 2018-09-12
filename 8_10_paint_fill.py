sc = [["r", "r", "g", "b"],
      ["r", "b", "g", "g"],
      ["r", "r", "g", "b"]]

def paint_fill(screen,r,c,nc,oc):
    if not screen: return None
    if r < 0 or c < 0 or r > len(screen)-1 or c > len(screen[0])-1:
        return None
    else:
        point_color = screen[r][c]
        if point_color == nc:
            return
        if point_color == oc:
            screen[r][c] = nc
            paint_fill(screen,r-1,c,nc,oc)
            paint_fill(screen,r+1,c,nc,oc)
            paint_fill(screen,r,c-1,nc,oc)
            paint_fill(screen,r,c+1,nc,oc)


paint_fill(sc,0,0,"Y","r")

for x in sc:
    print (x)
    

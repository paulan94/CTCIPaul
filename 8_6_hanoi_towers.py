def hanoi_towers(n,frm, to, spare):
    if n == 1:
        moveTo(frm, to)

    else:
        hanoi_towers(n-1,frm, spare, to)
        hanoi_towers(1,frm,to,spare)
        hanoi_towers(n-1, spare,to,frm)


def moveTo(frm, to):
    if not len(frm) == 0:
        frm_disk = frm.pop()
        print ("move {} to {}".format(frm_disk, to))
        to.append(frm_disk)


frm = [1,2,3,4,5,6,7]
to = []
spare = []

hanoi_towers(7,frm,to,spare)

print (frm, to, spare)

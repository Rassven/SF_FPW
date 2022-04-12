# Init
v_a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
vb = ["-", "O", "X"]
pl_num = 1
ch_res = 0
c_cou = 0
f_f = 0


# Draw
def vis_a(v_a):
    print()
    print("  0 1 2")
    for i in [0, 1, 2]:
        print(i, vb[v_a[i * 3]], vb[v_a[i * 3 + 1]], vb[v_a[i * 3 + 2]])


# Input
def ch_inp(i_str):
    ts = i_str.replace(" ", "")
    if len(ts) < 2:
        ts = ""
        return ts
    ts = ts[0] + ts[1] if ts[0] in "012" and ts[1] in "012" else ""
    return ts


# Check lines
def ch_lines(a):
    win_num = 0
    if a[0] * a[1] * a[2] == 1 or a[3] * a[4] * a[5] == 1 or a[6] * a[7] * a[8] == 1 or a[0] * a[3] * a[6] == 1 or a[
        1] * a[4] * a[7] == 1 or a[2] * a[5] * a[8] == 1 or a[0] * a[4] * a[8] == 1 or a[2] * a[4] * a[6] == 1:
        win_num = 1
    if a[0] * a[1] * a[2] == 8 or a[3] * a[4] * a[5] == 8 or a[6] * a[7] * a[8] == 8 or a[0] * a[3] * a[6] == 8 or a[
        1] * a[4] * a[7] == 8 or a[2] * a[5] * a[8] == 8 or a[0] * a[4] * a[8] == 8 or a[2] * a[4] * a[6] == 8:
        win_num = 2
    return win_num


# Main
vis_a(v_a)
while ch_res == 0 and f_f == 0:
    print("Player", pl_num, "(", vb[pl_num], "):")
    i_str = input("Input coordinates XY: ")
    res = str(ch_inp(i_str))
    while len(res) != 2:
        print("Incorrect")
        i_str = input("input coordinates XY: ")
        res = str(ch_inp(i_str))
    x = int(res[0])
    y = int(res[1])
    if v_a[x + y * 3] == 0:
        v_a[x + y * 3] = pl_num
        pl_num = 1 if pl_num > 1 else 2
    else:
        print("Already exist!")
    f_f = v_a[0] * v_a[1] * v_a[2] * v_a[3] * v_a[4] * v_a[5] * v_a[6] * v_a[7] * v_a[8]
    vis_a(v_a)
    ch_res = ch_lines(v_a)

# Results
if ch_res == 0:
    print("No winners")
elif ch_res == 1:
    print("O - winner")
elif ch_res == 2:
    print("X - winner")

def binaris_kereso(ls, searched):
    N = len(ls)
    also, felso = 0, N - 1
    while also <= felso:
        k = (felso + also) // 2
        if 70 < ls[k]:
            felso = k - 1
        elif 70 > ls[k]:
            also = k + 1
        else:
            return True, f"k = {k}, also = {also}, felso = {felso}"
    else:
        return False

print(binaris_kereso([2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91], 70))
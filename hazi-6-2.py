def palindrom(str):
    import copy
    str2 = copy.deepcopy(str)
    str2 = str2.lower()
    strrev = str2[::-1]
    strrev = strrev.replace('sc', 'cs').replace('zd', 'dz').replace('szd', 'dzs').replace('yg', 'gy').replace('yl', 'ly').replace('yn', 'ny').replace('zs', 'sz').replace('yt', 'ty').replace('sz', 'zs')
    if str2 == strrev:
        return f"{str2} == {strrev}\nYup, it's a palindrom."
    else:
        return 'Nope, not a palindrom, sorry!'

print(palindrom('arany nyara'))
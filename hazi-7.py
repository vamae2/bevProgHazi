import re

replace = ['"', '(', ')', ',', '-', '.', '?', '!',
    'a', 'e', 'i', 'o', 'u',
    'A', 'E', 'I', 'O', 'U',]
newtx = []
with open('hazi.txt', 'r') as fhand:
    x = 0
    for lin in fhand:
        if lin != '\n':
            lin = lin.rstrip()
            lin = re.sub(r'[^\x00-\x7f]',r'', lin) #removing non ascii characters
            for i in replace:
                lin = lin.replace(i, '')
            x += 1
            if x % 3 == 0:
                newtx.append(lin.lstrip())
        

with open('out.txt', 'w') as fhand2:
    fhand2.write('\n'.join(newtx))
# ====== Dictionary needed for function same ======
pr = {}

# ====== Object creation ======
class Team:
    def __init__(self, name, project, role):
        self.name = name
        self.project = project
        self.role = role
        pr[self.name] = self.project
        str = f"{self.name} is working on {self.project} in the role of {self.role}."
        print('--Developer created--\n' + str + '\n')

# ====== Function that writes out who works on the same project ======
def same():
    num = {}
    for x in pr:
        if pr[x] in num:
            num[pr[x]] += 1 
        else:
            num[pr[x]] = 1
    ls = []
    for y in num:
        if num[y] > 1:
            for z in pr:
                if y == pr[z]:
                    ls.append(z)
    st = ''
    if ls != []:
        for w in ls:
            st += w + ' and '
        st = st[:-4] + 'are working on the same project.\n'
        print(st)

# ====== Testing ======
ricsi = Team('Ricsi', 'SolArch', 'Frontend')
angela = Team('Angela', 'Zerteng', 'Tester')
peti = Team('Peti', 'KefERP', 'Backend')
eva = Team('Eva', 'KefERP', 'Frontend')
same()
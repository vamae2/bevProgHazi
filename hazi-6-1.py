def multiplication_table():
    firstline = '      1   2   3   4   5   6   7   8   9  10  11  12\n'
    lines = '  :-----------'
    x = -15
    for i in firstline:
        x += 1
    lines += ('-' * x) + '\n'
    ls = []
    table = ''
    for i in range(1, 13):
        if len(str(i)) == 1:
            table += f" {i}: "
        else:
            table += f"{i}: "
        for a in range(1, 13):
            if len(str(a * i)) == 1:
                table += f"  {a * i}"
            elif len(str(a * i)) == 2:
                table += f" {a * i}"
            else:
                table += f"{a * i}"
            if a != 12:
                table += ' '
            else:
                table += '\n'
    result = firstline + lines + table
    return result

print(multiplication_table())
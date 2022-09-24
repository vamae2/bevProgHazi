def converter():
    number = input('Write a number and unit (cm/inch): ')
    unit = input()
    retnum = ''
    retun = ''
    if unit != 'cm' and unit != 'inch':
        return 'Not correct unit!'
    if unit == 'cm':
        retnum = float(number) / 2.54
        retun = 'inch'
    else:
        retnum = float(number) * 2.54
        retun = 'cm'
    retnum = "{:.2f}".format(retnum)
    return f"{retnum} {retun}"

print(converter())
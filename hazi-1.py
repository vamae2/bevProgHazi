def wordsorter():
    sentence = input('Write a sencetnce: ')
    rev = sentence[::-1]
    proc = sentence.split()
    lst = []
    for b in proc:
        if b in lst:
            continue
        else:
            lst.append(b)
    letters = {}
    for i in sentence:
        for a in i:
            if a not in letters:
                letters[a] = 1
            else:
                letters[a] = letters[a] + 1
    letfreq = f"Frequency of letters: {letters}"
    lstwrd = f"Put into a list word by word: {lst}"
    reverse = f"Reversed: {rev}"
    return f"{letfreq}\n{reverse}\n{lstwrd}"

print(wordsorter())
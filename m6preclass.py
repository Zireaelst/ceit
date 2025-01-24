
def countCharInString(findChar, targetString):
    targetString = targetString.lower()
    findChar = findChar.lower()
    count = 0
    for char in targetString:
        if char == findChar:
            count += 1
    return count

print(countCharInString ('s', 'Mississippi'))
print(countCharInString ('p', 'Mississippi'))
print(countCharInString ('q', 'Mississippi'))
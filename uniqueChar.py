
def uniqueChar(str):

    emptySet = set()

    for letters in str:
        if letters in emptySet:
            return False
        else:
            emptySet.add(letters)

    return True


def uniqueChar1(str):
    
    emptyStr = ''
    
    for letters in str:
        if letters in emptyStr:
            return False
        else:
            emptyStr += letters
    
    return True

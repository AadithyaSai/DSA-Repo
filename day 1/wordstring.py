def isLower(c):
    return ord('a') <= ord(c) <= ord('z')

def isUpper(c):
    return ord('A') <= ord(c) <= ord('Z')
    
def toUpper(c):
    if isLower(c):
        return chr(ord(c) - 32)
    return c

def toLower(c):
    if isUpper(c):
        return chr(ord(c) + 32)
    return c

if __name__ == '__main__':
    s = input()

    isCaps = True
    word = ''

    for c in s:
        if c == ' ':
            print(word, end=' ')
            isCaps = not isCaps
            word = ''
        else:
            if isCaps:
                word = toUpper(c) + word
            else:
                word = toLower(c) + word

    print(word)


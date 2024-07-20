def isUpper(c):
    return ord('A') <= ord(c) <= ord('Z')

def toLower(c):
    if isUpper(c):
        return chr(ord(c) + 32)
    return c

def isPalindrome(s, start, end):
    i = start
    j = end

    while i != j:
        if toLower(s[i]) != toLower(s[j]):
            return False

        i += 1
        j -= 1

    return True

if __name__ == '__main__':
    s = input()

    start = 0
    for end in range(len(s)):
        if end + 1 == len(s) or s[end + 1] == ' ':
            if not isPalindrome(s, start, end):
                for k in range(start, end + 1):
                    print(s[k], end='')
                print(' ', end='')
            start = end + 2

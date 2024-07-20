def isAlpha(c):
    return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')

def isDigit(c):
    return ord('0') <= ord(c) <= ord('9')

if __name__ == "__main__":
    s = input()

    word = ''
    num = 0
    ans = ''

    for c in s:
        if isAlpha(c):
            if num:
                ans += word * num + " "
                num = 0
                word = ''
            word += c
        elif isDigit(c):
            num = 10 * num + ord(c) - ord('0')

    if num:
        ans += word * num

    print(ans)
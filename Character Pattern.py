

n = int(input())
i = 1
while i <= n:
    j = 1
    startP = chr(ord('A') + i - 1)
    while j<= i:
        #print jth column
        charP = chr(ord(startP) + j - 1)
        print(charP, end='')
        j = j + 1
    print()
    i = i + 1

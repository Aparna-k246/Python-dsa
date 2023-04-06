def permutation(str):
    if len(str) == 0:
        return [""]
    smallOutput=permutation(str[1:])
    output = []
    for i in range(len(smallOutput)):
        for j in range(len(smallOutput[i])+1):
           #start = str[i]
           remaining=smallOutput[i][:j]+str[0]+smallOutput[i][j:]      
           output.append(remaining)

    return output


string = input()
ans = permutation(string)
for s in ans:
    print(s)



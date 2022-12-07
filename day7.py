with open("day7.txt") as f:
    wordlist = [line.rstrip() for line in f]

splitter = "/"
directsplit = [splitter]
fullList = {splitter: 0}
allnumbers = 0


for x in wordlist:
    checkstring = x.split(" ")
    if [w for w in x.split()[1:] if x.startswith("$")]:
        if checkstring[2 - 1] == "cd":
            if checkstring[3 - 1] == "/":
                directsplit = [splitter]
            if checkstring[3 - 1] == "..":
                directsplit.pop()
            else:
                directsplit.append(checkstring[3 - 1])
                fullList[splitter.join(directsplit)] = 0
        elif checkstring[2 - 1] == "ls":
            #print(fullList)
            continue
    elif [w for w in x.split()[1:] if x.startswith("dir")]:
        continue
    else:
        fullList[splitter.join(directsplit)] += int(checkstring[0])
        allnumbers += int(checkstring[0])

        if len(directsplit) == 1:
            fullList[splitter] += int(checkstring[0])
        else:
            for x in range(len(directsplit) -1, 0, -1):
                fullList[splitter.join(directsplit[:x])] += int(checkstring[0])

number = 70000000 - allnumbers
mini = 30000000

awnser1 = sum(n for n in fullList.values() if n <= 100000)
awnser2 = min([n for n in fullList.values() if n + number >= mini])

print(awnser1)
print(awnser2)

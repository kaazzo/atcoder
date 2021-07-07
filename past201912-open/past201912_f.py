from sys import stdin

N = stdin.readline().rstrip("\n")

upper_idx = [index for index, n in enumerate(N) if n.isupper()]

words = []
for index, i in enumerate(upper_idx):
    if index % 2 != 0:
        continue
    elif index == len(upper_idx) - 2:
        words.append(N[i :])
    else:
        words.append(N[i : upper_idx[index + 2]])

words.sort(key=str.lower)

print(*words, sep="")

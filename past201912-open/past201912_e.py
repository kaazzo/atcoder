from sys import stdin
import numpy as np

N, Q = stdin.readline().split(" ")
logs = [stdin.readline().split(" ") for _ in range(int(Q))]

status = np.full((int(N), int(N)), "N", dtype=str)


def follow(user, target):
    if user == target:
        return None
    else:
        status[user, target] = "Y"


for log in logs:
    if log[0] == "1":
        follow(int(log[1]) - 1, int(log[2]) - 1)

    elif log[0] == "2":
        for index, s in enumerate(status[:, int(log[1]) - 1]):
            if s == "Y":
                follow(int(log[1]) - 1, index)

    elif log[0] == "3":
        follow_list = []
        for index, s in enumerate(status[int(log[1]) - 1]):
            if s == "Y":
                follow_list.append(index)
        #
        for f in follow_list:
            for index, i in enumerate(status[f]):
                if i == "Y":
                    follow(int(log[1]) - 1, index)

for s in status:
    print(*s, sep="")

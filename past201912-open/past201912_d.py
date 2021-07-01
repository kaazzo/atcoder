from sys import stdin

list_length = int(stdin.readline())
new_list = [int(stdin.readline()) for _ in range(list_length)]

if len(set(new_list)) == list_length:
    print("Correct")

else:
    new_list.sort()

    former_num = 0
    alt_num = 0
    for index, n in enumerate(new_list):

        if n == new_list[index - 1]:
            alt_num = n

        elif n - new_list[index - 1] >= 2:
            former_num = n - 1

    # 配列の隣り合う数字に2以上の差が存在しない場合,変更された数字は配列内の最大値で確定
    if former_num == 0:
        former_num = list_length

    print(str(alt_num) + " " + str(former_num))

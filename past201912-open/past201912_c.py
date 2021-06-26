input_list = input().split(" ")

num_list = sorted([int(s) for s in input_list], reverse=True)

print(num_list[2])

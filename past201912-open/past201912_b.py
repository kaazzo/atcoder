days = input()

price_list = []
for day in range(int(days)):
    sales = input()
    price_list.append(int(sales))

for index in range(len(price_list)):
    if index == 0:
        continue

    diff = price_list[index] - price_list[index - 1]
    if diff == 0:
        print("stay")
    elif diff > 0:
        print("up " + str(diff))
    else:
        print("down " + str(abs(diff)))

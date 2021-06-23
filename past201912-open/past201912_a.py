args = input()
try:
    print(int(args) * 2)
except ValueError as e:
    print("error")

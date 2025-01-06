def print_string(num):

    print(*[i if not i in num else 99 for i in range(3, 37, 3)])
    print(*[i if not i in num else 99 for i in range(2, 36, 3)])
    print(*[i if not i in num else 99 for i in range(1, 35, 3)])

    print(num)

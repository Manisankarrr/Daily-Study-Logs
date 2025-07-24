def star_pyramid(n):
    for i in range(n):
        if i % 2 != 0:
            continue
        print(' ' * (n - i - 1) + '* ' * (i + 1))

star_pyramid(7)

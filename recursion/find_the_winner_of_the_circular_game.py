
def circle_game(f, c):

    fl = [i for i in range(1,f + 1)]
    start = 0

    while len(fl) > 1:
        start += c - 1
        if len(fl) <= start:
            start %= len(fl)
        del fl[start]

    return fl[0]

if __name__ == '__main__':
    assert circle_game(5,2) == 3
    assert circle_game(6,5) == 1

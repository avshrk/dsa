
def circle_game(f, c):

    fl = [i + 1 for i in range(f)]
    idx = 0

    while len(fl) > 1:
        idx = (idx + c - 1) % len(fl)
        del fl[idx]

    return fl[0]

if __name__ == '__main__':
    assert circle_game(5,2) == 3
    assert circle_game(6,5) == 1

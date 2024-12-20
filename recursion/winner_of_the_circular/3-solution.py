
def circle_game(n, k):
    if n == 1:
        return 1

    pos = 0
    for i in range(2, n+1):
        pos = (pos + k) % i
    return pos + 1


if __name__ == '__main__':
    assert circle_game(5,2) == 3
    assert circle_game(6,5) == 1

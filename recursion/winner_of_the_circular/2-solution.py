
def circle_game(n, k):
    def circle(n):
        if n == 1:
            return 0
        return (circle(n - 1) + k) % n
    return circle(n) + 1


if __name__ == '__main__':
    assert circle_game(5,2) == 3
    assert circle_game(6,5) == 1


def solution(data: int):
    if data == 1:
        _sum = 2
    else:
        f55 = 1
        f59 = 1
        f95 = 1
        f99 = 1
        for i in range(data):
            n55 = f59
            n59 = f95 + f99
            n95 = f55 + f59
            n99 = f95

            f55 = n55
            f59 = n59
            f95 = n95
            f99 = n99
        _sum = f55 + f59 + f95 + f99
    return _sum


if __name__ == '__main__':
    print(solution(1))


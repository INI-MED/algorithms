from typing import List


def prefix(string: str) -> List[int]:
    P = [0] * len(string)
    j = 0
    i = 1

    while i < len(string):
        if string[j] != string[i]:
            if j > 0:
                j = P[j - 1]
            else:
                i += 1
        else:
            P[i] = j + 1
            i += 1
            j += 1

    return P


def kmp(substring: str, string: str) -> int:

    k = 0
    l = 0
    P = prefix(substring)

    while k < len(string):
        if substring[l] == string[k]:
            k += 1
            l += 1

            if l == len(substring):
                return k - len(substring)

        elif l > 0:
            l = P[l - 1]
        else:
            k += 1

    return -1


if __name__ == '__main__':
    s = "abcabeabcabcabd"
    sub = "abcabd"
    lsub = len(sub)
    index = kmp(sub, s)
    print(index)
    print(f"found: {s[index:index + lsub]} index: {index}")

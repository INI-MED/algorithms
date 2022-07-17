class LastOccur(object):

    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        return self.occurrences[letter]


def boyer_moore_match(text: str, pattern: str) -> int:
    alphabet = set(text)
    last = LastOccur(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1 + l)
            j = m - 1
    return -1


if __name__ == '__main__':

    def show_match(text: str, pattern: str) -> None:
        print(f'Text: {text}')
        p = boyer_moore_match(text, pattern)
        print(f'Match: {"."*p}{pattern}')


    text = 'abacaabadcabacabaabb'
    pattern = 'abacab'
    show_match(text, pattern)

    text = 'the result of boyer-moore algorithm'
    pattern = 'moor'
    show_match(text, pattern)
    show_match(text, pattern + 'e')

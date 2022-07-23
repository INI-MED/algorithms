

class SimHash:

    def __init__(self, tokens: str = '', hash_bits: int = 128):
        self.hash_bits = hash_bits
        self.hash = self.simhash(tokens)

    def __str__(self):
        return str(self.hash)

    def simhash(self, tokens):
        v = [0] * self.hash_bits
        for t in [self._string_hash(x) for x in tokens]:
            for i in range(self.hash_bits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1
                else:
                    v[i] -= 1
        fingerprint = 0
        for i in range(self.hash_bits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint

    def hamming_distance(self, other):
        x = (self.hash ^ other.hash) & ((1 << self.hash_bits) - 1)
        tot = 0
        while x:
            tot += 1
            x &= x - 1
        return tot

    def similarity(self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b:
            return b / a
        else:
            return a / b

    def _string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hash_bits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            return x


if __name__ == '__main__':
    s = 'This is a test string for testing'
    hash1 = SimHash(s.split())

    s = 'This is a test string for testing also'
    hash2 = SimHash(s.split())

    s = 'this string is a final test string'
    hash3 = SimHash(s.split())

    print(hash1.hamming_distance(hash2), "   ", hash1.similarity(hash2))
    print(hash1.hamming_distance(hash3), "   ", hash1.similarity(hash3))

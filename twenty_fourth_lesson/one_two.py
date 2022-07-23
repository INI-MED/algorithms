import re


class Solution:
    def __init__(self, line: str):
        self.line = line
        self.split_line = re.split("[/ +]", self.line)
        self.first_num = int(self.split_line[0])
        self.sec_num = int(self.split_line[1])
        self.third_num = int(self.split_line[2])
        self.forth_num = int(self.split_line[3])

        self.div = self.sec_num * self.forth_num
        self.sum = self.first_num * self.forth_num + self.third_num * self.sec_num

    def largest_common_divisor(self, a: int, b: int) -> int:
        return a if b == 0 else self.largest_common_divisor(b, a % b)


if __name__ == '__main__':
    ex = Solution("2/100+3/100")
    div = ex.div
    _sum = ex.sum
    print(ex.largest_common_divisor(div, _sum))

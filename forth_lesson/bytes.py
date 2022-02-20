
import ctypes


class King:
    def __init__(self):
        self.noA = 0xfefefefefefefefe
        self.noH = 0x7f7f7f7f7f7f7f7f

    def get_bitboard_moves(self, position: int) -> int:
        k = 1 << position

        # k = 1488
        ka = k & self.noA
        kh = k & self.noH
        mask = (ka << 7) | (k << 8) | (kh << 9) | (ka << 1) | (kh << 1) | (ka >> 9) | (k >> 8) | (kh >> 7)

        return mask

print(King().get_bitboard_moves(63))

"""
Занятие от 31.01.2022
"""
import sys
import math


def square_build(x: int, y: int) -> None:
    while True:
        print("for exit type 0")
        try:
            case = int(input(" choose the case (from 1 to 25): "))
            for row in range(x):
                for col in range(y):
                    x_coord = str(row) if case != 0 and col == 0 else ""
                    space = " " if len(x_coord) == 1 else ""
                    if case == 0:
                        sys.exit()
                    elif case == 1:
                        print(x_coord, space, "#" if row > col else "*", end="")
                    elif case == 2:
                        print(x_coord, space, "#" if row == col else "*", end="")
                    elif case == 3:
                        print(x_coord, space, "#" if row == 24 - col else "*", end="")
                    elif case == 4:
                        print(x_coord, space, "#" if row < 30 - col else "*", end="")
                    elif case == 5:
                        print(x_coord, space, "#" if row == math.floor(col/2) else "*", end="")
                    elif case == 6:
                        print(x_coord, space, "#" if row <= 9 or col <= 9 else "*", end="")
                    elif case == 7:
                        print(x_coord, space, "#" if row >= 15 and col >= 15 else "*", end="")
                    elif case == 8:
                        print(x_coord, space, "#" if row * col == 0 else "*", end="")
                    elif case == 9:
                        print(x_coord, space, "#" if math.fabs(row - col) >= 10 else "*", end="")
                    elif case == 10:
                        print(x_coord, space, "#" if math.floor(col/(row + 1)) == 1 else "*", end="")
                    elif case == 11:
                        print(x_coord, space, "#" if row == 1 or col == 1 or row == 23 or col == 23 else "*", end="")
                    elif case == 12:
                        print(x_coord, space, "#" if 5 <= col <= 19 and row == 15 else "*", end="")
                    elif case == 13:
                        print(x_coord, space, "#" if 20 <= row + col <= 28 else "*", end="")
                    elif case == 14:
                        print(x_coord, space, "#" if 5 <= col <= 19 and row == 15 else "*", end="")
                    elif case == 15:
                        print(x_coord, space, "#" if 10 <= math.fabs(row - col) <= 20 else "*", end="")
                    elif case == 16:
                        print(x_coord, space, "#" if 5 <= col <= 19 and row == 15 else "*", end="")
                    elif case == 17:
                        print(x_coord, space, "#" if math.sin(col/2) <= row/2 - 10 else "*", end="")
                    elif case == 18:
                        print(x_coord, space, "#" if row * col == col else "*", end="")
                    elif case == 19:
                        print(x_coord, space, "#" if row * col == 0 or row == 24 or col == 24 else "*", end="")
                    elif case == 20:
                        print(x_coord, space, "#" if (row + col) % 2 == 0 else "*", end="")
                    elif case == 21:
                        print(x_coord, space, "#" if 5 <= col <= 19 and row == 15 else "*", end="")
                    elif case == 22:
                        print(x_coord, space, "#" if (row + col) % 3 == 0 else "*", end="")
                    elif case == 23:
                        print(x_coord, space, "#" if 5 <= col <= 19 and row == 15 else "*", end="")
                    elif case == 24:
                        print(x_coord, space, "#" if 5 <= col <= 19 and row == 15 else "*", end="")
                    elif case == 25:
                        print(x_coord, space, "#" if 5 <= col <= 19 and row == 15 else "*", end="")
                    else:
                        print(f"no match for case number {case}")
                        continue
                print()

        except ValueError:
            print("wrong format. try again")


square_build(25, 25)

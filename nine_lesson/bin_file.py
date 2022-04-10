
def file_creation() -> None:
    with open("binary.bin", "wb") as file:
        file.write(bytearray([i for i in range(1, 255)]))


if __name__ == "__main__":
    file_creation()


"""
Given an array of integers, for each element determine whether that element occurs earlier in the array and whether 
it occurs later in the array. Create two strings of binary digits. In the first string, each character is a 1 if the 
value at that index also occurs earlier in the array, or 0 if not. In the second string, each character is a 1 if 
the value at that index occurs later in the array, or 0 if not. Return an array of two strings where the first string 
is related to lower indices and the second to higher.
"""
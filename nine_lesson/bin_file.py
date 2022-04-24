
def file_creation() -> None:
    with open("binary.bin", "wb") as file:
        for _ in range(1, 65536):
            file.write(bytearray([i for i in range(1, 255)]))


if __name__ == "__main__":
    file_creation()

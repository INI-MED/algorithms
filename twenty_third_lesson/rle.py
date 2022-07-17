def rle_encode(data: str) -> str:
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:

        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data: str) -> str:
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


if __name__ == '__main__':
    data = "some string"
    encode = rle_encode(data)
    print(encode)
    decode = rle_decode(encode)
    print(decode)

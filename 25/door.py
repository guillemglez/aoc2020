from typing import List

SUBJECT = 7
INPUT = (1526110, 20175123)


def encrypt(subject: int, loops: int) -> int:
    encrypted = 1
    for loop in range(loops):
        encrypted *= subject
        encrypted %= 20201227
    return encrypted


def find(key: int) -> int:
    encrypted = 1
    loop = 0
    while 1:
        encrypted *= 7
        encrypted %= 20201227
        loop += 1
        if encrypted == key:
            return loop


print(
    f"The encryption key {encrypt(INPUT[0], find(INPUT[1]))} is the handshake")

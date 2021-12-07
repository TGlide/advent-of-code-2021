from utils import getInputFileLines

lines = getInputFileLines("3")


def findMostCommonBits(numbers):
    bits = [{"0": 0, "1": 0} for i in range(len(numbers[0]))]
    for number in numbers:
        for digit in range(len(number)):
            bit = number[digit]
            bits[digit][bit] += 1

    result = []
    for bit in bits:
        result.append(max(bit, key=bit.get))
    return result


def inverseBits(bits):
    result = []
    for bit in bits:
        result.append("1" if bit == "0" else "0")
    return result


def binaryToDecimal(bits):
    result = 0
    for bit in bits:
        result = result * 2 + int(bit)
    return result


gamma_rate = ''.join(findMostCommonBits(lines))
print(gamma_rate)
epsilon_rate = ''.join(inverseBits(gamma_rate))
print(epsilon_rate)
print(binaryToDecimal(gamma_rate) * binaryToDecimal(epsilon_rate))

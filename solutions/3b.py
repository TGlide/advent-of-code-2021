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
        if bit["0"] > bit["1"]:
            result.append("0")
        elif bit["0"] <= bit["1"]:
            result.append("1")
    return result


def inverseBits(bits):
    result = []
    for bit in bits:
        result.append("1" if bit == "0" else "0")
    return result


def findUncommonBits(numbers):
    bits = findMostCommonBits(numbers)
    return inverseBits(bits)


def binaryToDecimal(bits):
    result = 0
    for bit in bits:
        result = result * 2 + int(bit)
    return result


def filterBits(numbers, compare_fn, bit=0):
    filteredBits = compare_fn(numbers)
    filteredNumbers = [
        numbers for numbers in numbers if numbers[bit] == filteredBits[bit]]

    if len(filteredNumbers) == 1:
        return filteredNumbers[0]
    else:
        return filterBits(filteredNumbers, compare_fn, bit + 1)


oxygenRating = filterBits(lines, findMostCommonBits)
print(oxygenRating)
co2Rating = filterBits(lines, findUncommonBits)
print(co2Rating)
print(binaryToDecimal(oxygenRating) * binaryToDecimal(co2Rating))

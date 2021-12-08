from utils import getInputFileLines


lines = getInputFileLines("5")


def getCoordinates(line: str):
    # Given a line "0,9 -> 5,9" return {x1: 0, y1: 9, x2: 5, y2: 9}
    coord1, coord2 = line.split(" -> ")
    x1, y1 = [int(num) for num in coord1.split(",")]
    x2, y2 = [int(num) for num in coord2.split(",")]
    return {
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,
    }


def isDiagonalCoord(coordinate):
    # Return true if the coordinate is diagonal
    return not (coordinate["x1"] == coordinate["x2"] or coordinate["y1"] == coordinate["y2"])


def filterDiagonalCoordinates(coordinates: list):
    # Given an array of coordinates, filter out the diagonal ones
    return [coord for coord in coordinates if not isDiagonalCoord(coord)]


def filterUnfitCoordinates(coordinates: list):
    # Given an array of coordinates, filter out the ones that don't fit
    result = []
    for coord in coordinates:
        if not isDiagonalCoord(coord):
            result.append(coord)
        else:
            x1, x2 = min(coord["x1"], coord["x2"]), max(
                coord["x1"], coord["x2"])
            y1, y2 = min(coord["y1"], coord["y2"]), max(
                coord["y1"], coord["y2"])
            if x2 - x1 == y2 - y1:
                result.append(coord)
    return result


def generateMatrix(coordinates: list):
    # Given an array of coordinates, generate a matrix filled with 0s
    matrix = []
    maxX = max([max(coord['x1'], coord['x2']) for coord in coordinates])
    maxY = max([max(coord["y1"], coord['y2']) for coord in coordinates])
    for _ in range(maxY + 1):
        matrix.append([0] * (maxX + 1))
    return matrix


def fillMatrix(matrix: list, coordinates: list):
    # Given a matrix and an array of coordinates, fill the matrix with 1s
    for coord in coordinates:

        if not isDiagonalCoord(coord):
            x1, x2 = min(coord["x1"], coord["x2"]), max(
                coord["x1"], coord["x2"])
            y1, y2 = min(coord["y1"], coord["y2"]), max(
                coord["y1"], coord["y2"])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    matrix[y][x] += 1
        else:
            x1, x2 = coord['x1'], coord['x2']
            y1, y2 = coord['y1'], coord['y2']

            x = x1
            y = y1
            for i in range(abs(x1 - x2) + 1):
                matrix[y][x] += 1
                x = x + 1 if x1 < x2 else x - 1
                y = y + 1 if y1 < y2 else y - 1

    return matrix


def printMatrix(matrix: list):
    # Print a matrix
    for rowIndex in range(len(matrix)):
        row = matrix[rowIndex]
        print(f"{rowIndex}:\t", end=" ")
        for point in row:
            print(point if point != 0 else '.', end=" ")
        print()
    print()


def getOverlappingPoints(matrix: list):
    # Given a matrix, return the number of points bigger than 1
    points = 0
    for row in matrix:
        for point in row:
            if point > 1:
                points += 1
    return points


# Part 1
print("Part 1:\n")

coordinates = [getCoordinates(line) for line in lines]
print("Coordinates:")
for coord in coordinates:
    print(coord)
print()

filteredCoordinates = filterDiagonalCoordinates(coordinates)
print("Filtered coordinates:")
for coord in filteredCoordinates:
    print(coord)
print()

matrix = generateMatrix(filteredCoordinates)
# printMatrix(matrix)

filledMatrix = fillMatrix(matrix, filteredCoordinates)
# printMatrix(filledMatrix)

overlappingPoints = getOverlappingPoints(filledMatrix)
print("Overlapping points:", overlappingPoints)

# Part 2
print("\nPart 2:\n")

filteredCoordinates = filterUnfitCoordinates(coordinates)
print("Filtered coordinates:")
for coord in filteredCoordinates:
    print(coord)
print()

matrix = generateMatrix(filteredCoordinates)
# printMatrix(matrix)

filledMatrix = fillMatrix(matrix, filteredCoordinates)
# printMatrix(filledMatrix)

overlappingPoints = getOverlappingPoints(filledMatrix)
print("Overlapping points:", overlappingPoints)

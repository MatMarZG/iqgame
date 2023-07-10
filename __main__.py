from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class Tile(Enum):
    NONE = 1
    HOLE = 2
    FILLED = 3


class Piece:
    def __init__(self, color: Color, shape: list[list[Tile]]):
        self.color = color
        self.shape = shape


def getPiecesFromText(filename: str):
    descriptionFile = open(filename, "r")
    pieces: list[Piece] = []
    currentColor: Color = None
    tileArray: list[list[Tile]] = []
    for line in descriptionFile:
        line = line.strip()
        match line:
            case "r":
                currentColor = Color.RED
            case "g":
                currentColor = Color.GREEN
            case "b":
                currentColor = Color.BLUE
            case "y":
                currentColor = Color.YELLOW
            case "---":
                pieces.append(Piece(currentColor, tileArray))
                currentColor: Color = None
                tileArray: list[list[Tile]] = []
            case _:
                currTileArray = []
                for char in line:
                    match char:
                        case "o":
                            currTileArray.append(Tile.HOLE)
                        case ".":
                            currTileArray.append(Tile.FILLED)
                        case " ":
                            currTileArray.append(Tile.NONE)
                tileArray.append(currTileArray)
    descriptionFile.close()
    return pieces


descFile = input("Enter file with tiles description: ")
print(getPiecesFromText(descFile))


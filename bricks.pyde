import style

# Define a couple of values
imWidth = 800  # Width of the image
imHeight = 600  # Height of the image
imPadding = imWidth / 32  # Padding on the side of the image
blockNumber = 28  # How many blocks in each direction
cellSize = float(imWidth - imPadding * 2) / blockNumber  # Calculate how big a cell is
rowNumber = int((imHeight - imPadding * 2) / cellSize)  # Calculate the number of rows
padding = cellSize / 4  # Calculate the padding
blockSize = cellSize - 2 * padding  # Calculate the block
blockOffset = blockSize / 5  # How much randomness the blocks have
strokeSize = blockSize / 6  # Size of the border

# TODO: select a style. Look into style.py to see what styles are available
s = style.Nord

# Setup the program
def setup():
    size(imWidth, imHeight)
    strokeWeight(strokeSize)
    noLoop()
    print("Press ENTER to save the image.")


# Create the blocks
def draw():
    background(s.background)
    cells = [[False for x in range(blockNumber)] for y in range(blockNumber)]

    for row in range(rowNumber):
        for col in range(blockNumber):
            # Draw the 2x2 blocks
            if random(1) < 0.2:
                i, j = randomCell(rowNumber - 1, blockNumber - 1)
                if (
                    not cells[i][j]
                    and not cells[i + 1][j]
                    and not cells[i][j + 1]
                    and not cells[i + 1][j + 1]
                ):
                    y = i * cellSize + padding + imPadding
                    x = j * cellSize + padding + imPadding
                    drawBlock(
                        x, y, blockSize * 2 + 2 * padding, blockSize * 2 + 2 * padding,
                    )
                    cells[i][j] = cells[i + 1][j] = cells[i][j + 1] = cells[i + 1][
                        j + 1
                    ] = True

            # Draw the 2x1 blocks
            if random(1) < 0.3:
                i, j = randomCell(rowNumber, blockNumber - 1)
                if not cells[i][j] and not cells[i][j + 1]:
                    y = i * cellSize + padding + imPadding
                    x = j * cellSize + padding + imPadding
                    drawBlock(x, y, blockSize * 2 + 2 * padding, blockSize)
                    cells[i][j] = cells[i][j + 1] = True

            # Draw the 1x2 blocks
            if random(1) < 0.3:
                i, j = randomCell(rowNumber - 1, blockNumber)
                if not cells[i][j] and not cells[i + 1][j]:
                    y = i * cellSize + padding + imPadding
                    x = j * cellSize + padding + imPadding
                    drawBlock(x, y, blockSize, blockSize * 2 + 2 * padding)
                    cells[i][j] = cells[i + 1][j] = True

    # Fill the gaps with 1x1 blocks
    for row in range(rowNumber):
        for col in range(blockNumber):
            if cells[row][col] == True:
                continue
            y = row * cellSize + padding + imPadding
            x = col * cellSize + padding + imPadding
            drawBlock(x, y, blockSize, blockSize)


# Draw a block
def drawBlock(x, y, w, h):
    # Draw the color
    noStroke()
    fill(randomColor())
    beginShape()
    vertex(randomPoint(x, y))
    vertex(randomPoint(x + w, y))
    vertex(randomPoint(x + w, y + h))
    vertex(randomPoint(x, y + h))
    endShape(CLOSE)

    # Draw the border
    if not s.disableBorder:
        strokeJoin(ROUND)
        stroke(s.stroke)
        noFill()
        beginShape()
        vertex(randomPoint(x, y))
        vertex(randomPoint(x + w, y))
        vertex(randomPoint(x + w, y + h))
        vertex(randomPoint(x, y + h))
        endShape(CLOSE)


# Get a random cell
def randomCell(a, b):
    return (int(random(a)), int(random(b)))


# Randomize the points x and y
def randomPoint(x, y):
    x += random(-blockOffset, blockOffset)
    y += random(-blockOffset, blockOffset)
    return (x, y)


# Return a random color
def randomColor():
    return unhex(s.alpha + s.colors[int(random(len(s.colors)))])


def keyPressed():
    if key == ENTER or key == RETURN:
        selectOutput("Where to save the image ?", "saveFile")
    if key == " ":
        redraw()
    if key == "n":
        global s
        s = style.randomStyle()
        redraw()


def saveFile(selected):
    save(str(selected))
    print("Saved file at:" + str(selected))

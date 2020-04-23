import style

# Define a couple of values
# TODO: Please change them to your needs
imWidth = 800  # Width of the image
imHeight = 600  # Height of the image
imPaddingWidth = imWidth / 30  # Padding on the left and rigth side of the image
blockNumber = 28  # How many blocks in each direction
cellSize = float(imWidth - imPaddingWidth * 2) / blockNumber  # Calculate how big a cell is
rowNumber = int((imHeight - imPaddingWidth * 2) / cellSize)  # Calculate the number of rows
imPaddingHeight = (imHeight - cellSize * rowNumber) / 2.0 # Calculate the top and bottom padding
padding = cellSize / 4  # Calculate the padding
blockSize = cellSize - 2 * padding  # Calculate the blocksize
blockOffset = blockSize / 5  # How much randomness the blocks have
strokeSize = blockSize / 6  # Size of the border

# TODO: select a style. Look into style.py to see what styles are available
s = style.One

# Setup the program
def setup():
    size(imWidth, imHeight)
    strokeWeight(strokeSize)
    noLoop()
    print("Current Style: " + s.name)
    print("Press ENTER to save the image.")


# Create the blocks
def draw():
    background(s.background)
    
    # Keep track of which cells are already filled
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
                    y = i * cellSize + padding + imPaddingHeight
                    x = j * cellSize + padding + imPaddingWidth
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
                    y = i * cellSize + padding + imPaddingHeight
                    x = j * cellSize + padding + imPaddingWidth
                    drawBlock(x, y, blockSize * 2 + 2 * padding, blockSize)
                    cells[i][j] = cells[i][j + 1] = True

            # Draw the 1x2 blocks
            if random(1) < 0.3:
                i, j = randomCell(rowNumber - 1, blockNumber)
                if not cells[i][j] and not cells[i + 1][j]:
                    y = i * cellSize + padding + imPaddingHeight
                    x = j * cellSize + padding + imPaddingWidth
                    drawBlock(x, y, blockSize, blockSize * 2 + 2 * padding)
                    cells[i][j] = cells[i + 1][j] = True

    # Fill the gaps with 1x1 blocks
    for row in range(rowNumber):
        for col in range(blockNumber):
            # Ignore cells that are already filled
            if cells[row][col] == True:
                continue
            y = row * cellSize + padding + imPaddingHeight
            x = col * cellSize + padding + imPaddingWidth
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

# Listen for key, presses
def keyPressed():
    # Save the image
    if key == ENTER or key == RETURN:
        selectOutput("Where to save the image ?", "saveFile")

    # Redraw the shapes
    if key == " ":
        redraw()

    # Set to a random color scheme
    if key == "n":
        global s
        s = style.randomStyle()
        print("Change style to: " + s.name)
        redraw()

# Save the file 
def saveFile(selected):
    save(str(selected))
    print("Saved file at:" + str(selected))

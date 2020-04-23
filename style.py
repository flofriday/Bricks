class Style:
    def __init__(self, background, stroke, disableBorder, alpha, colors):
        self.background = background
        self.stroke = stroke
        self.disableBorder = disableBorder
        self.alpha = alpha
        self.colors = colors

NO_ALPHA = "FF"



# Note: Use a border
Default = Style(
    background=255,
    stroke=0,
    disableBorder = False,
    alpha=hex(70),
    colors=["FF0000", "00FF00", "0000FF"],
)

# Inspired by: https://draculatheme.com/
# Note: Don't use a border
Dracula = Style(
    background=unhex("282a36"),
    stroke=unhex("f8f8f2"),
    disableBorder = True,
    alpha=NO_ALPHA,
    colors=[
        "8be9fd",
        "50fa7b",
        "ffb86c",
        "ff79c6",
        "bd93f9",
        "ff5555",
        "f1fa8c",
    ],
)

# Inspired by: https://www.nordtheme.com/
# Note: Use a border
Nord = Style(
    background=unhex("eceff4"),
    stroke=unhex(NO_ALPHA + "2e3440"),
    disableBorder = False,
    alpha=NO_ALPHA,
    colors=["8fbcbb", "88c0d0", "81a1c1", "5e81ac",],
)

Styles = [Default, Dracula, Nord]

def randomStyle():
    return Styles[int(random(len(Styles)))]

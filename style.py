# Dear Contributor,
# Two rules: 
#   1. first insert a new styles alphabetically
#   2. add the new style to the `Styles` list at the bottom of this file


# A basic class to store all relevant informations
class Style:
    def __init__(self, name, background, stroke, disableBorder, alpha, colors):
        self.name = name
        self.background = background
        self.stroke = stroke
        self.disableBorder = disableBorder
        self.alpha = alpha
        self.colors = colors


# A simple constant
NO_ALPHA = "FF"


# Default color scheme for testing
Default = Style(
    name="Default",
    background=255,
    stroke=0,
    disableBorder=False,
    alpha=hex(70),
    colors=["FF0000", "00FF00", "0000FF"],
)

# Inspired by: https://draculatheme.com/
Dracula = Style(
    name="Dracula",
    background=unhex("282a36"),
    stroke=unhex("f8f8f2"),
    disableBorder=True,
    alpha=NO_ALPHA,
    colors=["8be9fd", "50fa7b", "ffb86c", "ff79c6", "bd93f9", "ff5555", "f1fa8c",],
)

# Inspired by: https://www.nordtheme.com/
Nord = Style(
    name="Nord",
    background=unhex("eceff4"),
    stroke=unhex(NO_ALPHA + "2e3440"),
    disableBorder=False,
    alpha=NO_ALPHA,
    colors=["8fbcbb", "88c0d0", "81a1c1", "5e81ac",],
)

# Inspired by: https://github.com/joshdick/onedark.vim
One = Style(
    name="One",
    background=unhex("282C34"),
    stroke=unhex(NO_ALPHA + "ABB2BF"),
    disableBorder=True,
    alpha=NO_ALPHA,
    colors=["E06C75", "98C379", "E5C07B", "61AFEF",],
)

# Inspired by: https://ethanschoonover.com/solarized/
Solarized = Style(
    name="Solarized",
    background=unhex("fdf6e3"),
    stroke=unhex(NO_ALPHA + "073642"),
    disableBorder=False,
    alpha="AA",
    # Colors are: yellow, orange, red, magenta, violet, blue, cyan, green
    colors=[
        "b58900",
        "cb4b16",
        "dc322f",
        "d33682",
        "6c71c4",
        "268bd2",
        "2aa198",
        "859900",
    ],
)

# Inspired by: https://ethanschoonover.com/solarized/
Solarized_Dark = Style(
    name="Solarized_Dark",
    background=unhex("002b36"),
    stroke=unhex(NO_ALPHA + "93a1a1"),
    disableBorder=False,
    alpha="88",
    # Colors are: yellow, orange, red, magenta, violet, blue, cyan, green
    colors=[
        "b58900",
        "cb4b16",
        "dc322f",
        "d33682",
        "6c71c4",
        "268bd2",
        "2aa198",
        "859900",
    ],
)

# A list of all styles
Styles = [Default, Dracula, One, Nord, Solarized, Solarized_Dark]


def randomStyle():
    return Styles[int(random(len(Styles)))]

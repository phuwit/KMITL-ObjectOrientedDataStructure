# *** Fun with Drawing ***
# Enter input : 2
# .*.*.
# *+*+*
# .*+*.
# ..*..

# *** Fun with Drawing ***
# Enter input : 5
# ....*.......*....
# ...*+*.....*+*...
# ..*+++*...*+++*..
# .*+++++*.*+++++*.
# *+++++++*+++++++*
# .*+++++++++++++*.
# ..*+++++++++++*..
# ...*+++++++++*...
# ....*+++++++*....
# .....*+++++*.....
# ......*+++*......
# .......*+*.......
# ........*........

# 4 1 7 1 4
# 3 3 5 3 3
# 2 5 3 5 2
# 1 7 1 7 1
# 17


# *** Fun with Drawing ***
# Enter input : 7
# ......*...........*......
# .....*+*.........*+*.....
# ....*+++*.......*+++*....
# ...*+++++*.....*+++++*...
# ..*+++++++*...*+++++++*..
# .*+++++++++*.*+++++++++*.
# *+++++++++++*+++++++++++*
# .*+++++++++++++++++++++*.
# ..*+++++++++++++++++++*..
# ...*+++++++++++++++++*...
# ....*+++++++++++++++*....
# .....*+++++++++++++*.....
# ......*+++++++++++*......
# .......*+++++++++*.......
# ........*+++++++*........
# .........*+++++*.........
# ..........*+++*..........
# ...........*+*...........
# ............*............


from typing import List


CHAR_EMPTY = "."
CHAR_BORDER = "*"
CHAR_INSIDES = "+"


def create_layer(meat_width: int):
    layer: str = ""
    layer += CHAR_BORDER
    meat_width -= 2
    if meat_width <= 0:
        return layer
    layer += meat_width * CHAR_INSIDES
    layer += CHAR_BORDER
    return layer


def create_double_spikes(height: int):
    layers: List[str] = []
    for empty_side_width in range(height - 1, -1, -1):
        meat_width = ((height - empty_side_width) * 2) - 1
        empty_middle_width = (empty_side_width * 2) - 1

        layer: str = ""

        layer += CHAR_EMPTY * empty_side_width
        layer += create_layer(meat_width)
        layer += CHAR_EMPTY * empty_middle_width
        if empty_side_width == 0:
            layer += create_layer(meat_width)[1::]
        else:
            layer += create_layer(meat_width)
        layer += CHAR_EMPTY * empty_side_width

        layers.append(layer)
    return layers


def create_inverted_triangle(total_width: int):
    empty_side_width = 1
    layers: List[str] = []
    for meat_width in range(total_width - 1, 0, -2):
        layer: str = ""
        layer += CHAR_EMPTY * empty_side_width
        layer += create_layer(meat_width)
        layer += CHAR_EMPTY * empty_side_width
        empty_side_width += 1
        layers.append(layer)
    return layers


print("*** Fun with Drawing ***")
size = int(input("Enter input : "))

top_layers = create_double_spikes(size)
bottom_layers = create_inverted_triangle(len(top_layers[-1]) - 1)

print("\n".join(top_layers))
print("\n".join(bottom_layers))

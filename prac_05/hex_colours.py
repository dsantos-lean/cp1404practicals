NAME_TO_CODE = {"Amber": "#ffbf00", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Army Green": "#4b5320", "Ash Grey": "#b2beb5", "Asparagus": "#87a96b", "Banana Yellow": "#ffe135", "Beaver": "#9f8170", "Bitter Lime": "#bfff00", "Bittersweet Shimmer": "#bf4f51"}
colour_name = input("Colour name: ")
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(f"{colour_name} is {NAME_TO_CODE[colour_name]}")
    colour_name = input("Colour name: ")

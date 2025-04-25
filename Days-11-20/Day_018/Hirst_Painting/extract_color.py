# Use Colorgram package (https://pypi.org/project/colorgram.py/) to extract colors from spots.jpg and put the extracted color tuples (rgb) into a list.
import colorgram

colors = colorgram.extract('spots.jpg', 10)
color_pallet = []

for color in colors:
    color_r = color.rgb.r
    color_g = color.rgb.g
    color_b = color.rgb.b
    color_pallet.append((color_r, color_g, color_b))

print(color_pallet)

# instructor code
# rgb_colors = []
# colors = colorgram.extract('spots.jpg', 8)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_pallet.append(new_color)
#
# print(rgb_colors)
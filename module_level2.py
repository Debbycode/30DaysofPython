import random


print('=====================One========================')

def list_of_hexa_colors(number_of_colors):
    hexa_colors = []
    for i in range(number_of_colors):
        color = "#"
        for j in range(6):
            color += random.choice("0123456789ABCDEF")
        hexa_colors.append(color)
    return hexa_colors


print('=====================Two========================')


def list_of_rgb_colors(number_of_colors):
    rgb_colors = []
    for i in range(number_of_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        rgb_colors.append((red, green, blue))
    return rgb_colors


print('=====================Three========================')


def generate_colors(number_of_colors, color_format):
    if color_format == "hex":
        return list_of_hexa_colors(number_of_colors)
    elif color_format == "rgb":
        return list_of_rgb_colors(number_of_colors)



number_of_colors = 5
color_format = "hex"
colors = generate_colors(number_of_colors, color_format)
print("Hexadecimal colors:", colors)

number_of_colors = 5
color_format = "rgb"
colors = generate_colors(number_of_colors, color_format)
print(f'RGB colors: {color_format}{colors}')

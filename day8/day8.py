

import time


width = 25
height = 6
layer_size = width * height


def read():
    return ''.join(open("input").readline().split('\n'))


input = read()
image_size = len(input)


def print_image(image):
    print("▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅")
    for row in image:
        row_content = ""
        time.sleep(0.50)
        print("▅  "+row_content.join(row).replace('0', ' ').replace('1', '▅')+" ▅")
    print("▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅")


def part2(layers):
    image = [['2'] * width for height in range(0, height)]

    for layer in layers:
        layer_rows = [layer[start:start+width]
                      for start in range(0, layer_size, width)]
        for col in range(0, width):
            for row in range(0, height):
                if image[row][col] == '2' and layer_rows[row][col] < '2':
                    image[row][col] = layer_rows[row][col]

    print_image(image)


def part1():
    layers = list(
        map(lambda x: input[x:x+layer_size], range(0, image_size, layer_size)))
    segments_with_zero_counts = list(map(lambda x: (x, x.count('0')), layers))
    target_layer = sorted(segments_with_zero_counts, key=lambda x: x[1])[0][0]
    print(target_layer.count('1') * target_layer.count('2'))
    return layers


def main():

    layers = part1()
    part2(layers)


main()

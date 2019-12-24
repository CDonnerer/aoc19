"""Day 8 of AoC. Image data parsing.
"""
import numpy as np

example_input = "123456789012"


def parse_image(image: str, width: int, height: int):
    split_img = [pixel for pixel in image]
    n_layers = int(len(split_img) / (width * height))

    layers = list()
    start = 0
    stop = width

    for _ in range(n_layers):
        layer = np.zeros(shape=(height, width))

        for j in range(height):
            layer[j, :] = split_img[start:stop]
            start += width
            stop += width

        layers.append(layer)

    return layers


def load_input(path="input.dat"):
    return str(np.loadtxt(path, dtype=str))


def main():
    """
    """
    image = load_input()

    layers = parse_image(image=image, width=25, height=6)
    l_zeros = list()

    for layer in layers:
        n_zeros = sum(sum(layer == 0))
        l_zeros.append(n_zeros)

    fewest_zeros = np.array(l_zeros).argmin()

    n_ones = sum(sum(layers[fewest_zeros] == 1))
    n_twos = sum(sum(layers[fewest_zeros] == 2))

    print(n_ones, n_twos, n_ones * n_twos)


if __name__ == "__main__":
    main()

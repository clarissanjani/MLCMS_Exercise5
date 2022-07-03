from collections import deque


def import_data(file):
    """
    :param file: file to import
    :return: float tuple array containing the data points of the input file
    """
    data = []
    with open(file) as f:
        for line in f.readlines():
            elem1, elem2 = line.split()
            x1 = str(elem1)
            x2 = x1.replace(',', '.')
            y1 = str(elem2)
            y2 = y1.replace(',', '.')
            data.append((float(x2), float(y2)))
    return data


def shift_data(x, delta_t):
    """
    :param x: input data/ axis
    :param delta_t: #rows the data is rotated/ delayed
    :return: x rotated by delta_t rows to the left
    """
    x_shifted = deque(x)
    # a negative delta_t shifts the axis from right to left
    # i.e. delays the data
    x_shifted.rotate(-delta_t)
    return x_shifted

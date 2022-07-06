from collections import deque


def import_data(file):
    """
    :param file: file to import
    :return: float tuple array containing columns of the input file
    """
    data = []
    with open(file) as f:
        # skip first line
        f.readline()
        for line in f.readlines():
            elem0, elem1, elem2, elem3, elem4, elem5, elem6, elem7, elem8, elem9 = line.split()
            x1 = str(elem1)
            x2 = x1.replace(',', '.')
            y1 = str(elem2)
            y2 = y1.replace(',', '.')
            z1 = str(elem3)
            z2 = z1.replace(',', '.')
            data.append((int(x2), int(y2), int(z2)))
    return data


def create_delay_embedding(data, starting_index, num_delays):
    """
    :param data: input data
    :param starting_index: row in the data array where the window starts
    :param num_delays: specifies the number of rows per window
    :return: a delay embedding of size num_delays starting at starting_index
    """
    return data[starting_index:starting_index + num_delays]


def vectorize_delay_embedding(e):
    """
    :param e: delay_embedding to be vectorized, e.g. array(351, 3)
    :return: a vectorized delay embedding of size rows x columns, e.g. array(1053)
    """
    return list(sum(e, ()))


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


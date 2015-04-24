"""Usage:
    scale.py DATA_SET
    scale.py -h | --help
Options:
    -h --help    show this help message
"""
from docopt import docopt

class Scale:
    def __init__(self, min_values, max_values):
        if len(min_values) == len(max_values):
            try:
                for value in min_values:
                    float(value)
                for value in max_values:
                    float(value)
            except ValueError:
                raise ValueError('Scales must be representable as floats')
            self._min_values = min_values
            self._max_values = max_values
        else:
            raise ValueError('Scales do not match in size')
    def __str__(self):
        return repr([self.min_values, self.max_values])
    @property
    def min_values(self):
        return self._min_values
    @property
    def max_values(self):
        return self._max_values
    @property
    def list_repr(self):
        return [self.min_values, self.max_values]


def scale(filename, delim=','):
    """Returns a Scale, the min_values element being the list of minimum
    and the max_values element being the list of maximum values of the
    attributes.

    The index of a nested list represents which attribute.
    """
    min_values = []
    max_values = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            line_separated = line.split(delim)
            for index, value in enumerate(line_separated):
                if len(min_values) <= index:
                    min_values.append(float('inf'))
                    max_values.append(float('-inf'))
                value = float(value)
                if value < min_values[index]:
                    min_values[index] = value
                if value > max_values[index]:
                    max_values[index] = value
    return Scale(min_values, max_values)

if __name__ == "__main__":
    args = docopt(__doc__)
    print(scale(args['DATA_SET']))

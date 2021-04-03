#!/usr/bin/python
import sys
from commands import *


if __name__ == "__main__":

    # Validate input
    valid_args(sys.argv)
    valid_grid(sys.argv[1])
    valid_locations(sys.argv[1], sys.argv[2:])
    # Deliver pizza
    print(deliver_pizza(sys.argv[2:]))

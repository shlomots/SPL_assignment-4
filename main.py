import sys

from Repository import _Repository
import initialize
from DTOs import *


def main():
    config = sys.argv[1]
    orders = sys.argv[2]
    output = sys.argv[3]
    repo = _Repository(sys.argv[4])
    repo.create_tables()
    initialize.initialize(config, repo)
    repo.parse_orders(orders)
    repo.create_output(output)


if __name__ == '__main__':
    main()



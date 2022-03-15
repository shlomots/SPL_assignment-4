from DTOs import *


def initialize(path, repo):
    file = open(path, 'r')
    content = file.read()
    config_lines = content.split("\n")
    num_of_hats = 0
    for i in range(len(config_lines)):
        line = config_lines[i].split(",")
        if i == 0:
            num_of_hats = int(line[0])
        elif i <= num_of_hats:
            hat = Hat(int(line[0]), line[1], int(line[2]), int(line[3]))
            repo.hats.insert(hat)
        else:
            supplier = Supplier(int(line[0]), line[1])
            repo.suppliers.insert(supplier)
        repo.commit()

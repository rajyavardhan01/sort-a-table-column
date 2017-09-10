#!/bin/python3

import operator

if __name__ == "__main__":

    line = input().split(' ')
    rows = int(line[0])
    cols = int(line[1])

    table = []

    for i in range(rows):
        line = input().split(' ')
        table.append([int(x) for x in line])

    sort_key = int(input())
    table.sort(key=operator.itemgetter(sort_key))

    for row in table:
        print(' '.join(str(x) for x in row))
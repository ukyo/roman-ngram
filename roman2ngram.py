#!/usr/bin/python
#coding: utf8

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz-,.'
row = [a for a in alphabet]
spliter = ' '

def print_row_label():
    return spliter + spliter.join(row)

def build_col_label(n):
    short_col = []
    if n > 2:
        short_col = ['^']
        short_col_ = short_col[:]
        for i in range(n - 3):
            short_col__ = short_col_[:]
            for x in short_col__:
                for y in row:
                    short_col__.append(x + y)
            short_col_ = short_col__
            short_col.extend(short_col_)

    col = ['^'] + row
    for i in range(n - 2):
        col_ = []
        for x in col:
            for y in row:
                col_.append(x + y)
        col = col_
    short_col.extend(col)
    return short_col

def build_table(x, y):
    zeros = [0 for i in range(x)]
    return [zeros[:] for i in range(y)]

def count(line, n, table, col):
    history = ['' for i in range(n - 2)]
    history.append('^')
    for c in line[:-1]:
        try:
            table[col.index(''.join(history))][row.index(c)] += 1
            history = history[1:]
            history.append(c)
        except:
            pass

def print_table_iter(table, col):
    yield print_row_label()
    for i, v in enumerate(table):
        yield col[i] + spliter + spliter.join([str(x) for x in v])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'error'
        quit()

    n = int(sys.argv[1])
    if n < 2:
        print 'not support unigram'
        quit()

    col = build_col_label(n)
    table = build_table(len(row), len(col))
    for line in sys.stdin:
        count(line, n, table, col)

    for line in print_table_iter(table, col):
        sys.stdout.write(line + '\n')

#!/usr/bin/python
#coding: utf8

'''
This script convert Katakana to Roman.

Required:
    romkan.py
'''

import sys
import romkan
import re

p = re.compile('\'')
p2 = re.compile('。')
p3 = re.compile('、')
sub = p.sub
sub2 = p2.sub
sub3 = p3.sub


def conv_line(line):
    try:
        return sub3(',', sub2('.', sub('', romkan.to_kunrei(romkan.to_roma(unicode(line, ('utf8'))).encode('utf8')))))
    except:
        return ''

def conv(input_file):
    return (conv_line(line) for line in input_file)

if __name__ == '__main__':
    for line in conv(sys.stdin):
        try:
            sys.stdout.write(line)
        except:
            pass

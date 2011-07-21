#!/usr/bin/python
#coding: utf8

'''
This script convert Japanese text(Kanji, Hiragana, etc...) to Katakana.

Required:
    mecab
    mecab-ipadic(utf-8)
    mecab-python
'''

import sys
import re
import MeCab

p_ruby = re.compile('《.+?》')
p_hira = re.compile('[ァ-ヶー]+')
sub = p_ruby.sub
match = p_hira.match
m = MeCab.Tagger()
kigou = set(['「','」','、','・','？','…','　','々','〜'])


def conv_line(line):
    tmp = sub('', line)
    tmp = m.parse(tmp)
    lst = []
    for _line in tmp.split('\n')[:-2]:
        feature = _line.split(',')
        if len(feature) < 8:
            continue
        yomi = feature[7]
        if yomi == '。':
            lst.append('。\n')
        elif yomi == '、':
            lst.append('、')
        elif '記号' in _line:
            pass
        elif match(yomi):
            lst.append(yomi)
    return ''.join(lst)

def conv(input_file):
    return (conv_line(line) for line in input_file)

if __name__ == '__main__':
    help_text = '''
Usage: python text2hira.py [OPTION...]

-i, --input       input file
-o, --output      output file
'''
    
    input_file_name = None
    output_file_name = None
    if len(sys.argv) != 1:
        try:
            index = None
            if '-i' in sys.argv:
                index = sys.argv.index('-i')
            elif '--input' in sys.argv:
                index = sys.argv.index('--index')
            if index:
                input_file_name = sys.argv[index + 1]
            
            index = None
            if '-o' in sys.argv:
                index = sys.argv.index('-o')
            elif '--output' in sys.argv:
                index = sys.argv.index('--output')
            if index:
                output_file_name = sys.argv[index + 1]
        except:
            print help_text

    input_file = open(input_file_name) if input_file_name else sys.stdin
    output_file = open(output_file_name, 'w') if output_file_name else sys.stdout

    for line in conv(input_file):
        output_file.write(line + '\n')

    input_file.close()
    output_file.close()

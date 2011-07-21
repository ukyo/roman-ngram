#!/bin/sh

./text2kata.py < $1 | ./kata2roman.py | ./roman2ngram.py $2


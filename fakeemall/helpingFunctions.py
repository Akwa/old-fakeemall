#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *

"""
Helping functions
"""

def hexToDec(x):
    """
    Simply an int() function with closed second arg.
    """
    return int(x, 16)

def processData(byteSeq):
    """
    If input is one byte, outputs its decimal value.
    Eg. input '\x64' (something like exp yield) outputs 100.

    If input is more than one byte, outputs list of ints.
    Eg. input '\x00\x00' (normal-normal type) outputs [0, 0].
    Other example, Celebi basestats:
    '\x64\x64\x64\x64\x64\x64' or 'dddddd'
    map(ord, 'dddddd') = [100, 100, 100, 100, 100, 100]
    """
    if len(byteSeq) == 1:
        return ord(byteSeq)
    return map(ord, byteSeq)

def processEggGroup(byteSeq):
    """
    2 egg groups are contained in 1 byte.
    Changes int type input to nice, two-int egg-group list.
    """
    byteSeq = processData(byteSeq)
    return map(hexToDec, '%x' % byteSeq)

def processTms(byteSeq):
    """
    Converts every byte into string of 0-1's,
    then makes it a list of 8 0-1 ints.
    Code might be ugly, but hey it works.
    """
    tms = []
    byteSeq = processData(byteSeq)
    for tmByte in byteSeq:
        # bin(int) returns string starting with '0b'
        # tms are put in reversed order, eg. (8, 7, ..., 1)
        # '0b' is cut out and string reversed with [:1:-1]
        # extra zeros have to be added if less than 8 digits
        tmByte = format(tmByte, '#010b')[:1:-1]
        # str to list (eg. '00001111' to [0, 0, 0, 0, 1, 1, 1, 1])
        tmByte = map(int, tmByte)
        tms.extend(tmByte)
    return tms

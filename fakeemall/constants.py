#!/usr/bin/env python
# -*- coding: utf-8 -*-
maxPokemon = 251
maxMoves = 251
maxTms = 61

lenBasestat = 32
lenMove = 7
lenPalette = 8
lenName = 10
lenMovename = 10
lenTm = 1
lenPointer = 2
lenBank = 0x4000

bitsPerByte = 8
evoLengths = {'\x01': 3, '\x02': 3, '\x03': 3, '\x04': 3, '\x05': 4}

alph = {
"\x50": "@",
"\x54": "#",
"\x7f": " ",
"\x80": "A",
"\x81": "B",
"\x82": "C",
"\x83": "D",
"\x84": "E",
"\x85": "F",
"\x86": "G",
"\x87": "H",
"\x88": "I",
"\x89": "J",
"\x8a": "K",
"\x8b": "L",
"\x8c": "M",
"\x8d": "N",
"\x8e": "O",
"\x8f": "P",
"\x90": "Q",
"\x91": "R",
"\x92": "S",
"\x93": "T",
"\x94": "U",
"\x95": "V",
"\x96": "W",
"\x97": "X",
"\x98": "Y",
"\x99": "Z",
"\x9a": "(",
"\x9b": ")",
"\x9c": ":",
"\x9d": ";",
"\x9e": "[",
"\x9f": "]",
"\xa0": "a",
"\xa1": "b",
"\xa2": "c",
"\xa3": "d",
"\xa4": "e",
"\xa5": "f",
"\xa6": "g",
"\xa7": "h",
"\xa8": "i",
"\xa9": "j",
"\xaa": "k",
"\xab": "l",
"\xac": "m",
"\xad": "n",
"\xae": "o",
"\xaf": "p",
"\xb0": "q",
"\xb1": "r",
"\xb2": "s",
"\xb3": "t",
"\xb4": "u",
"\xb5": "v",
"\xb6": "w",
"\xb7": "x",
"\xb8": "y",
"\xb9": "z",
"\xd0": "'d",
"\xd1": "'l",
"\xd2": "'m",
"\xd3": "'r",
"\xd4": "'s",
"\xd5": "'t",
"\xd6": "'v",
"\xe0": "'",
"\xe3": "-",
"\xe6": "?",
"\xe7": "!",
"\xe8": ".",
"\xe9": "&",
"\xef": "^",  # male-sign
"\xf3": "/",
"\xf4": ",",
"\xf6": "0",
"\xf7": "1",
"\xf8": "2",
"\xf9": "3",
"\xfa": "4",
"\xfb": "5",
"\xfc": "6",
"\xfd": "7",
"\xf5": "*",   # female-sign
"\xfe": "8",
"\xff": "9"
}

alphRev = {val: key for key, val in alph.items()}  # reverse alphabet

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from struct import pack, unpack
from itertools import izip

"""
Helping functions
"""

def bankEnd(offset):
    return offset + lenBank - offset % lenBank

def processName(byteSeq):
    """
    Translate every byte of our sequence if possible
    Then, ''.join() this list of translated chars
    """
    charList = []
    for byte in byteSeq:
        if byte == '\x50': # \x50 terminates name
            break
        charList.append(alph[byte])
    return ''.join(charList)

def processData(byteSeq):
    """
    If input is one byte, outputs its decimal value.
    Eg. input '\x64' (something like exp yield) outputs 100.

    If input is more than one byte, outputs list of ints.
    Eg. input '\x00\x00' (normal-normal type) outputs [0, 0].
    Other example, Celebi basestats:
    '\x64\x64\x64\x64\x64\x64' or 'dddddd'
    [ord(item) for item in 'dddddd'] = [100, 100, 100, 100, 100, 100]
    """
    if len(byteSeq) == 1:
        return ord(byteSeq)
    return [ord(item) for item in byteSeq]

def processEggGroup(byteSeq):
    """
    2 egg groups are contained in 1 byte.
    Changes int type input to nice, two-int egg-group list.
    """
    byteSeq = processData(byteSeq)
    return [int(item, 16) for item in '%x' % byteSeq]

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
        tmByte = [int(item) for item in tmByte]
        tms.extend(tmByte)
    return tms

def processPalettes(byteSeq):
    """
    Changes the 8-byte sequence to list of four lists [R, G, B].
    Every Pokemon palette data uses 8 bytes:
    4 for normal palette and 4 for shiny palette.
    These 4 bytes code 2 colors of every palette.
    So, 2 bytes (16 bits) denote 1 color.
    Each intensity of RGB uses 5 bits:
    GGGRRRRR 0BBBBBGG
    Green color is stored in:
    * first three bits of first byte
    * last two bits of second byte
    First bit of second byte is ignored (always 0)
    Following are some bit-wise operations extracting this data.
    """
    palettes = []
    byteSeq = processData(byteSeq)
    for i in xrange(0, lenPalette, 2):
        # two bytes, denoted as a and b
        a, b = byteSeq[i: i + 2]
        R = a & 0b00011111
        G = (a >> 0b101) + (b & 0b00000011) * 0b1000
        B = b >> 0b10
        palettes.append([R, G, B])
    return palettes

def processPointer(byteSeq, minus=0):
    """
    Reads the little-endian pointer and subtracts optional minus value.
    Minus value is the starting offset of some data in bank.
    Eg. Pokemon evomoves data starts at 0x425B1 in Crystal.
    0x25B1 must be subtracted from the all evomove pointers to find
    the relative position of place being pointed to by pointer.
    Bulbasaur pointer is A767.
    0x67A7 - 0x4000 - 0x25b1 = 0x1F6 = 502
    502 points to first index after all 251 pointers.
    """
    return unpack('<H', byteSeq)[0] - lenBank - minus

def nameRev(name):
    return ''.join((alphRev[char] for char in name))

def packBasestats(pokemon, i):
    stats = [i + 1]  # Pokemon are numbered from 1, not 0
    stats.extend(pokemon.stats)
    stats.extend(pokemon.types)
    stats.append(pokemon.catchRate)
    stats.append(pokemon.expYield)
    stats.extend(pokemon.wildHeldItems)
    stats.append(pokemon.genderRatio)
    stats.append(0x64)  # "unknown"
    stats.append(pokemon.eggCycles)
    stats.append(0x5)  # "unknown"
    stats.append(pokemon.dimensions)
    stats.extend((0, 0, 0, 0))
    stats.append(pokemon.growthRate)
    stats.append(packEggGroup(pokemon.eggGroups))
    stats.extend(packTms(pokemon.tms))
    return ''.join((chr(i) for i in stats))

def packEggGroup(eggGroup):
    return int(''.join((hex(i)[2:] for i in eggGroup)), 16)

def packTms(tms):
    data = []
    for i in xrange(0, 64, 8):  # magic numbers to be changed
        byte = ''.join(str(i) for i in reversed(tms[i:i + 8]))
        byte = int(byte, 2)
        data.append(byte)
    return data

def packMoves(move):
    stats = []
    stats.append(move.animation)
    stats.append(move.effect)
    stats.append(move.power)
    stats.append(move.type)
    stats.append(move.accuracy)
    stats.append(move.pp)
    stats.append(move.effectChance)
    return ''.join((chr(i) for i in stats))

def packPalettes(palette):
    data = []
    for r, g, b in palette:  # four palettes, two normal/two shiny
        a = chr(R + (G & 0b00111) * 0b100000)
        b = chr((G >> 3) + B * 0b100)
        data.append(''.join((a, b)))
    return ''.join(data)

def makePointer(address):
    return pack('<H', address + lenBank)

def packEvomoves(evos, moves):
    data = []
    lenData = 0
    for evo in evos:
        evo[-1] += 1  # indexing starts from 1 not 0
        data.append(''.join([chr(item) for item in evo]))
        lenData += len(evo)
    data.append('\x00')
    for move in moves:
        data.append(''.join([chr(item) for item in move]))
        lenData += 2
    data.append('\x00')
    lenData += 2
    return data, lenData

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
import random

class Pokemon(object):
    pass

class PokemonContainer(object):

    def __init__(self):
        self.pokemon = {i: Pokemon() for i in xrange(maxPokemon)}

    def __getitem__(self, item):
        return self.pokemon[item]

    def extractNames(self, data):
        """
        From the flat name sequence, extracts 10 bytes per iteration.
        Translates from bytecode to normal letters.
        """
        null = '\x50'
        for i in xrange(maxPokemon):
            j = i * lenName
            # byteSeq is the sequence of 10 bytes
            byteSeq = data[j:j + lenName]
            # translate every byte of our sequence if possible
            # then, ''.join() this list of translated chars
            name = ''.join([alph[b] for b in byteSeq if b != null])
            # Assign the name
            self.pokemon[i].name = name

    def extractBasestats(self, data):
        """
        Extracts basestats into our poke-classes.
        Some of these stats might be unneeded in randomization,
        but they are extracted anyway to help in future testing.
        """
        hexToDec = lambda x: int(x, 16)
        for i in xrange(maxPokemon):
            j = i * lenBasestat
            # byteSeq is the sequence of 32 bytes
            byteSeq = data[j:j + lenBasestat]
            # extract certain stats from certain locations.
            # *** Base stats ***
            # cut out the stats and make them an int list
            # eg. Celebi: map(ord, 'dddddd') = [100, ..., 100]
            stats = map(ord, byteSeq[0x1:0x7])
            self.pokemon[i].stats = stats
            # *** Types ***
            # similarly, uses map to change str into int list
            types = map(ord, byteSeq[0x7:0x9])
            self.pokemon[i].types = types
            # *** Catch rate ***
            catchRate = ord(byteSeq[0x9])
            self.pokemon[i].catchRate = catchRate
            # *** Exp yield ***
            expYield = ord(byteSeq[0xa])
            self.pokemon[i].expYield = expYield
            # *** Wild held items ***
            wildHeldItems = map(ord, byteSeq[0xb:0xd])
            self.pokemon[i].wildHeldItems = wildHeldItems
            # *** Gender ratio ***
            genderRatio = ord(byteSeq[0xd])
            self.pokemon[i].genderRatio = genderRatio
            # *** Egg cycles ***
            eggCycles = ord(byteSeq[0xf])
            self.pokemon[i].eggCycles = eggCycles
            # *** Dimensions ***
            dimensions = ord(byteSeq[0x11])
            self.pokemon[i].dimensions = dimensions
            # *** Growth Rate ***
            growthRate = ord(byteSeq[0x16])
            self.pokemon[i].growthRate = growthRate
            # *** Egg groups ***
            # had no idea right now how to extract it 'nicely'
            # because 2 egg groups are contained in 1 byte
            eggGroups = ord(byteSeq[0x17])
            eggGroups = map(hexToDec, '%x' % eggGroups)
            self.pokemon[i].eggGroups = eggGroups
            # *** TM/HM flags ***
            # this probably is ugly but works...
            # converts every byte into string of 0-1's
            # then makes it a list of 8 0-1 ints.
            tms = [0] * 64
            for b, byte in enumerate(byteSeq[0x18:0x20]):
                byte = ord(byte)
                # bin(int) returns string starting with '0b'
                # tms are put in reversed order, eg. (8, 7, ..., 1)
                # '0b' is cut out and string reversed with [:1:-1]
                byte = bin(byte)[:1:-1]
                byte = map(int, byte)
                tms[b*8:8 + b*8] = byte
            self.pokemon[i].tms = tms[:]

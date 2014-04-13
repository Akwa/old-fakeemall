#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from helpingFunctions import *
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
        for i in xrange(maxPokemon):
            j = i * lenName
            # byteSeq is the sequence of 10 bytes
            byteSeq = data[j:j + lenName]
            self.pokemon[i].name = processName(byteSeq)

    def extractBasestats(self, data):
        """
        Extracts basestats into our poke-classes.
        Some of these stats might be unneeded in randomization,
        but they are extracted anyway to help in future testing.
        """
        for i in xrange(maxPokemon):
            j = i * lenBasestat
            # byteSeq is the sequence of 32 bytes
            byteSeq = data[j:j + lenBasestat]

            # *** Base stats ***
            self.pokemon[i].stats = processData(byteSeq[0x1:0x7])

            # *** Types ***
            self.pokemon[i].types = processData(byteSeq[0x7:0x9])

            # *** Catch rate ***
            self.pokemon[i].catchRate = processData(byteSeq[0x9])

            # *** Exp yield ***
            self.pokemon[i].expYield = processData(byteSeq[0xa])

            # *** Wild held items ***
            self.pokemon[i].wildHeldItems = processData(byteSeq[0xb:0xd])

            # *** Gender ratio ***
            self.pokemon[i].genderRatio = processData(byteSeq[0xd])

            # *** Egg cycles ***
            self.pokemon[i].eggCycles = processData(byteSeq[0xf])

            # *** Dimensions ***
            self.pokemon[i].dimensions = processData(byteSeq[0x11])

            # *** Growth Rate ***
            self.pokemon[i].growthRate = processData(byteSeq[0x16])

            # *** Egg groups ***
            self.pokemon[i].eggGroups = processEggGroup(byteSeq[0x17])

            # *** TM/HM flags ***
            self.pokemon[i].tms = processTms(byteSeq[0x18:0x20])

    def extractPalettes(self, data):
        """
        Extracts the palettes data. You can read info about extracting
        palettes at helpingFunctions.processPalettes
        """
        for i in xrange(maxPokemon):
            j = i * lenPalette
            # byteSeq is the 8-byte sequence of single palette data.
            byteSeq = data[j:j + lenPalette]
            self.pokemon[i].palettes = processPalettes(byteSeq)

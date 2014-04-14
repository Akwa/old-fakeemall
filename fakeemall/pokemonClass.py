#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from helpingFunctions import *

class Pokemon(object):

    def __init__(self):
        self.evos = []
        self.prevos = []
        self.moves = {}

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


    def extractEvomoves(self, data, dataStart):
        """
        Extracts evolution and movesets data along with pointers.
        First 502 bytes (2*maxPokemon) are expected to be pointers.
        dataStart is needed as a reference to know where the pointers
        point.
        """
        dataStart = dataStart % lenBank + lenBank
        for i in xrange(maxPokemon):
            j = i * 2
            byteSeq = data[j:j + lenPointer]
            self.pokemon[i].pointer = processPointer(byteSeq, dataStart)
            k = self.pokemon[i].pointer
            while data[k] != '\x00':
                evoLength = evoLengths[data[k]]
                evoData = [ord(item) for item in data[k:k + evoLength]]
                evoData[-1] -= 1
                self.pokemon[i].evos.append(evoData)
                self.pokemon[evoData[-1]].prevos.append(i)
                k += evoLength
            k += 1
            while data[k] != '\x00':
                level, move = [ord(item) for item in data[k:k + 2]]
                self.pokemon[i].moves.setdefault(level, []).append(move)
                k += 2

    def updateNames(self):
        """
        Packs all the names into 10-byte long sequences.
        """
        data = []
        for i in xrange(maxPokemon):
            name = self.pokemon[i].name
            data.append(nameRev(name).ljust(10, '\x50'))
        return ''.join(data)

    def updateBasestats(self):
        """
        """
        data = []
        for i in xrange(maxPokemon):
            data.append(packBasestats(self.pokemon[i], i))
        return ''.join(data)

    def updatePalettes(self):
        """
        """
        pass

    def updateEvomoves(self):
        """
        """
        pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from helpingFunctions import *

class Pokemon(object):

    def __init__(self):
        self.evos = []
        self.prevos = []  # list = more than 1 parent possible
        self.moves = []
        self.familyLen = 0

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


    def extractEvomoves(self, data, evoStart):
        """
        Extracts evolution and movesets data along with pointers.
        First 502 bytes (2*maxPokemon) are expected to be pointers.
        dataStart is needed as a reference to know where the pointers
        point.
        """
        self.evoStart = evoStart % lenBank
        for i in xrange(maxPokemon):
            j = i * 2
            byteSeq = data[j:j + lenPointer]
            self.pokemon[i].pointer = processPointer(byteSeq, self.evoStart)
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
                self.pokemon[i].moves.append([level, move])
                k += 2
        self.depthSearch()

    def depthSearch(self):
        """
        Counts the length of each evolutionary line, finds the "parents"
        (first forms).
        An important but hopefully unnecessary assumption is no cyclic
        families and that each evolutionary line in each family has same
        length.
        """
        for i in xrange(maxPokemon):
            if not self.pokemon[i].prevos:
                self.depthSearchVisit(i, 0)

    def depthSearchVisit(self, i, stage):
        """
        Visits next Pokemon in evolutionary line.
        Increments "stage" attribute
        """
        newStage = stage + 1
        self.pokemon[i].stage = newStage
        if self.pokemon[i].evos:
            for evo in self.pokemon[i].evos:
                j = evo[-1]
                self.depthSearchVisit(j, newStage)
        else:
            self.backwardsVisit(i, newStage)

    def backwardsVisit(self, i, stage):
        """
        Visits preceding Pokemon in evolutionary line.
        Gives information of family length back to the top.
        """
        self.pokemon[i].familyLen = stage
        for parent in self.pokemon[i].prevos:
            # Let's assume for future than one day someone makes
            # evolutionary family where 2 predecessors are possible.
            if not self.pokemon[parent].familyLen:
                self.backwardsVisit(parent, stage)

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
        Packs the 3 color intensities into two bytes.
        Each color is defined by 5 bits plus there's one empty bit.
        """
        data = []
        for i in xrange(maxPokemon):
            data.append(packPalettes(self.pokemon[i].palettes))
        return ''.join(data)

    def updateEvomoves(self, start, end):
        """
        """
        totalLength = end - start
        evoData = []
        data = []
        lenData = self.evoStart + lenPointer * maxPokemon
        for i in xrange(maxPokemon):
            evoData.append(makePointer(lenData))
            evomoves, lenEvomoves = packEvomoves(self.pokemon[i].evos,
                                                 self.pokemon[i].moves)
            lenData += lenEvomoves
            data.append(evomoves)
        evoData.extend(data)
        evoData = ''.join((''.join(item) for item in evoData))
        evoData = evoData.ljust(totalLength, '\x00')
        return evoData

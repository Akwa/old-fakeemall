#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from helpingFunctions import *

class Move(object):
    pass

class MoveContainer(object):

    def __init__(self):
        self.moves = {i: Move() for i in xrange(maxMoves)}

    def __getitem__(self, item):
        return self.moves[item]

    def extractMovenames(self, data):
        """
        Extracts move names from bytecode.
        Move names don't use 10 bytes each, like Pokemon names
        and different method is required for their extraction.
        """
        i, m = 0, 0
        lenData = len(data)
        while i < lenData and m < maxMoves:
            moveName = []
            char = data[i]
            while char != '\x50':
                moveName.append(alph[char])
                i += 1
                char = data[i]
            moveName = ''.join(moveName)
            self.moves[m].name = moveName
            i += 1
            m += 1

    def extractMoves(self, data):
        """
        Extracts statistics of each move.
        1st byte: animation
        2nd byte: effect
        3rd byte: power
        4th byte: type
        5th byte: accuracy * (100/255)%
        6th byte: pp
        7th byte: effect change * (100/255)%
        """
        for i in xrange(maxMoves):
            j = i * lenMove
            # byteSeq is the sequence of 7 bytes
            byteSeq = data[j:j + lenMove]
            byteSeq = processData(byteSeq)
            self.moves[i].animation = byteSeq[0]
            self.moves[i].effect = byteSeq[1]
            self.moves[i].power = byteSeq[2]
            self.moves[i].type = byteSeq[3]
            self.moves[i].accuracy = byteSeq[4]
            self.moves[i].pp = byteSeq[5]
            self.moves[i].effectChance = byteSeq[6]

    def extractTms(self, data):
        """
        Extracts TM data - which TM responds to which move.
        First 50 entries are TMs 01 - 50, then 7 HMs.
        In Gold/Silver, last 4 bytes are empty.
        In crystal, first 3 of last 4 bytes are Move Tutor moves.
        """
        self.tmData = processData(data)

    def updateMovenames(self, start, end):
        """
        Packs the names into sequence of bytes.
        """
        totalLength = end - start
        data = []
        for i in xrange(maxMoves):
            data.append(nameRev(self.moves[i].name))
        data.append('')  # so the data ends with '\x50'
        return '\x50'.join(data).ljust(totalLength, '\x00')

    def updateMoves(self):
        """
        Packs all the move stats into sequence of bytes.
        """
        data = []
        for i in xrange(maxMoves):
            data.append(packMoves(self.moves[i]))
        return ''.join(data)

    def updateTms(self):
        """
        Returns 61 bytes of tm data, each byte denoting one tm.
        """
        return ''.join((chr(i) for i in self.tmData))

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
            
        

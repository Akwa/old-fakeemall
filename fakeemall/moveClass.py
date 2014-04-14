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
        

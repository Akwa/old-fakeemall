#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
import random

class Pokemon(object):

    def extractNames(self, data):
        """
        From the flat name sequence, extracts 10 bytes per iteration.
        Translates from bytecode to normal letters and finally,
        creates a dict with Pokémon names.
        """
        lenData = len(data)
        self.names = {}
        # lenData should be 2510, lenName is 10
        # so this xrange looks like (0, 10, 20, ..., 2500)
        for i in xrange(0, lenData, lenName):
            # charSeq is the sequence of 10 bytes
            byteSeq = data[i:i + lenName]
            # translate every byte of our sequence if possible
            # then, ''.join() this list of translated chars
            name = ''.join([alph[b] for b in byteSeq if b != '\x50'])
            # Add a new entry to our name dict
            self.names[len(self.names)] = name

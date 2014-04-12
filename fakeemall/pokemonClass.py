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
        Translates from bytecode to normal letters and finally,
        creates a dict with Pokémon names.
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

            
        

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from re import match

class Rom(object):

    def __init__(self, path, outPath='fakeem.gbc'):
        """
        Input path and output path is set here.
        """
        self.outPath = outPath
        self.readRom(path)
        self.parseRom()

    def readRom(self, path):
        """
        Pretty self-explanatory, reads the .gbc file
        from given path in binary mode.
        """
        with open(path, 'rb') as rom:
            self.data = rom.read()

    def parseRom(self):
        """
        Reads the game version from rom header.
        Sets the values of pointers depending on game version.
        Loads data from these pointers.
        Creates proper class instances from the "flat" data.
        """
        self.readVersion()
        self.setPointers()
        self.loadData()

    def readVersion(self):
        """
        Reads a part from rom header (offsets 0x134 to 0x13e).
        Establishes self.version attribute basing on content of it.
        """
        hdrStart = 0x134
        hdrEnd = 0x13e
        header = self.data[hdrStart:hdrEnd]
        self.version = {'POKEMON_GL': 'Gold',
                        'POKEMON_SL': 'Silver',
                        'PM_CRYSTAL': 'Crystal'
                        }.get(header)

    def overwriteRom(self):
        """
        Overwrites 'self.data*' attrs with new randomized data,
        assembles it back to 'self.data' and creates a new .gbc file.
        """
        self.updateDatas()
        self.assemblyData()
        with open(self.outPath, 'wb') as rom:
            rom.write(self.data)

    
    def setPointers(self):
        """
        Depending on version, selects particular pointers
        for particular data blocks.
        """
        # Evolution and moveset index bounds
        evomovesStart = {'Gold' : 0x42790,
                         'Silver' : 0x42790,
                         'Crystal': 0x42584
                         }.get(self.version)
        evomovesEnd = 0x44000  # Reserving the tail of bank
        self.pntEvomoves = (evomovesStart, evomovesEnd)

        # Base stats index bounds
        basestatsStart = {'Gold' : 0x51b0b,
                          'Silver' : 0x51b0b,
                          'Crystal': 0x51424
                          }.get(self.version)
        basestatsEnd = basestatsStart + maxPokemon * lenBasestat
        self.pntBasestats = (basestatsStart, basestatsEnd)

        # Moves data index bounds
        movesStart = {'Gold' : 0x41afe,
                      'Silver' : 0x41afe,
                      'Crystal': 0x41afb
                      }.get(self.version)
        movesEnd = movesStart + maxMoves * lenMove
        self.pntMoves = (movesStart, movesEnd)

        # Palette data index bounds
        palettesStart = {'Gold' : 0xad45,
                         'Silver' : 0xad45,
                         'Crystal': 0xad86
                         }.get(self.version)
        palettesEnd = palettesStart + maxPokemon * lenPalette
        self.pntPalettes = (palettesStart, palettesEnd)

        # Pokémon names data index bounds
        namesStart = {'Gold' : 0x1b0b74,
                      'Silver' : 0x1b0b74,
                      'Crystal': 0x53384
                      }.get(self.version)
        namesEnd = namesStart + maxPokemon * lenName
        self.pntNames = (namesStart, namesEnd)

        # Move names data index bounds
        movenamesStart = {'Gold' : 0x1b1574,
                          'Silver' : 0x1b1574,
                          'Crystal': 0x1c9f29
                          }.get(self.version)
        movenamesEnd = movenamesStart + maxMoves * lenMovename
        self.pntMovenames = (movenamesStart, movenamesEnd)

        # Moves TM data index bounds
        tmStart = {'Gold' : 0x11a66,
                   'Silver' : 0x11a66,
                   'Crystal': 0x1167a
                   }.get(self.version)
        tmEnd = tmStart + maxTms * lenTm
        self.pntTms = (tmStart, tmEnd)

    def loadData(self):
        """
        Having the pointers established, loads "flat" data from rom.
        """
        self.dataEvomoves = self.data.__getslice__(*self.pntEvomoves)
        self.dataBasestats = self.data.__getslice__(*self.pntBasestats)
        self.dataMoves = self.data.__getslice__(*self.pntMoves)
        self.dataPalettes = self.data.__getslice__(*self.pntPalettes)
        self.dataNames = self.data.__getslice__(*self.pntNames)
        self.dataMovenames = self.data.__getslice__(*self.pntMovenames)
        self.dataTms = self.data.__getslice__(*self.pntTms)

    def updateDatas(self):
        """
        The 'self.data*' attrs contain the "byte sequences" of data.
        This function extracts new random data from classes and updates
        the 'self.data*' attr with data converted to "byte sequence".
        """
        pass
    
    def assemblyData(self):
        """
        This piece of code overwrites the 'self.data'
        (the whole 2MBs of data) by sorting the data blocks in order.
        Puts unchanged blocks (not randomized parts) between that data.
        """
        pntPat = 'pnt[A-Z]{1}[a-zA-Z]*'
        dataPat = 'data[A-Z]{1}[a-zA-Z]*'
        
        # Grab all 'self.data*' and 'self.pnt*' attrs and sort them
        items = self.__dict__.iteritems
        allDatas = [v for k, v in sorted(items()) if match(dataPat, k)]
        allPnts = [v for k, v in sorted(items()) if match(pntPat, k)]
        allZipped = sorted(zip(allPnts, allDatas))

        # Assembly of rom using sorted data
        newdata = ''
        k = 0
        for (i, j), data in allZipped:
            newdata += self.data[k:i]
            newdata += data
            k = j
        else:
            newdata += self.data[j:]
        self.data = newdata

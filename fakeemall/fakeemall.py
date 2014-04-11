#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
random.seed(None)
import sys
from romClass import Rom

if __name__ == "__main__":
    lenArgv = len(sys.argv)
    if lenArgv > 1:
        path = sys.argv[1]
        if lenArgv > 2:
            outPath = sys.argv[2]
        else:
            outPath = None

        Data = Rom(path, outpath)

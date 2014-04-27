#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import pygsc
import sys
import helping_functions as h
import random
random_seed = h.generate_seed()
random.seed(random_seed)
import pokemon_randomization as p
import move_randomization as m

def fake_rom(path, out_path):
    Game = pygsc.rom_class.Rom(path, out_path)

    p.fake_pokemon(Game.pokemon)
    Game.save_data()

    pygsc.test.diff_roms.differences(path, out_path)
    print(random_seed)

if __name__ == '__main__':
    len_argv = len(sys.argv)
    if len_argv > 1:
        path = sys.argv[1]
        if len_argv > 2:
            out_path = sys.argv[2]
        else:
            out_path = 'fakeemall.gbc'
        fake_rom(path, out_path)
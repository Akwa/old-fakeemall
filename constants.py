#! /usr/bin/env python3
# -*- coding: utf-8 -*-

starters = (152, 155, 158)
legendaries = (144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251)

possible_types = [0, 1, 2, 3, 4, 5, 7, 8, 9,  # physical types
                  20, 21, 22, 23, 24, 25, 26, 27  # special types
                  ]

"""Predefined alpha and beta parameters of beta distribution"""
beta_standard = (2, 2)
beta_tight = (2.5, 2.5)
beta_right_tilted = (2, 1)  # mean is equal to 2/3
beta_left_tilted = (1, 2)  # mean is equal to 1/3

one_stage_exp_yield = {
    1: (-35, 0.41),
    }
two_stage_exp_yield = {
    1: (-24, 0.32),
    2: (-79, 0.52),
    }
two_stage_strong_exp_yield = {
    1: (-14, 0.32),
    2: (-63, 0.52),
    }
three_stage_exp_yield = {
    1: (0, 0.24),
    2: (-4, 0.35),
    3: (10, 0.36),
    }

"""
Some egg groups need to have types assigned to them, so randomization
has some sense. Not giving Pidgey flying-type or not giving Magikarp
water-type is way more misleading than not giving Rhyhorn rock-type.
This means some Pokemon will have predefined types.
"""
egg_group_types = {
    2: 21,  # amphibian group - water type
    3: 7,  # insect group - bug type
    4: 2,  # avian group - flying type
    7: 22,  # plant group - grass type
    9: 21,  # invertebrate group - water type
    12: 21,  # fish group - water type
    }

"""
These Pokemon are excluded from assigning certain types because of
their egg group.
Add only first stages of evolutionary line.
"""
egg_group_exceptions = [
    7,  # Squirtle (doesn't need to have obligatory water type)
    55,  # Psyduck
    79,  # Slowpoke
    84,  # Doduo (has no wings so it can be non-flying sometimes)
    98,  # Krabby
    120,  # Staryu
    138,  # Omanyte
    140,  # Kabuto
    147,  # Dratini
    152,  # Chikorita
    158,  # Totodile
    225,  # Delibird
    ]

# Subtract 1 from all IDs because of 0-based indexing in Python
egg_group_exceptions = [i - 1 for i in egg_group_exceptions]
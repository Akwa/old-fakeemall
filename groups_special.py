#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import constants as fc
from pygsc import constants as c

"""
Special groups are handled differently from normal groups.
WARNING: The order of these groups matters.
If Eevee group is defined after branched groups, it won't work :D
"""
groups_special = [
    {
        'name': 'Starters',
        'length': 3,
        'id': fc.starters,
        'stats': {
            1: (308, 12, fc.beta_standard),
            2: (90, 10, fc.beta_standard),
            3: (106, 14, fc.beta_standard),
            },
        'catch_rate': {
            1: 45,
            2: 45,
            3: 45,
            },
        'exp_yield': {
            1: (0, 0.21),
            2: (-60, 0.5),
            3: (91, 0.22),
            },
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_slow'],
    },
    {
        'name': 'Legendaries',
        'length': 1,
        'id': fc.legendaries,
        'stats': {
            1: (580, 100, fc.beta_standard),
            },
        'catch_rate': {
            1: 3,
            },
        'exp_yield': {
            1: (193, 0.04),
            },
        'egg_cycles': 120,
        'growth_rate': c.growth_rates['slow'],
    },
    {
        'name': 'Eevee',
        'length': 2,
        'special_evo': True,
        'id': (133,),
        'stats': {
            1: (315, 30, fc.beta_tight),
            2: (185, 30, fc.beta_tight),
            },
        'catch_rate': {
            1: 45,
            2: 45,
            },
        'exp_yield': fc.two_stage_exp_yield,
        'egg_cycles': 35,
        'growth_rate': c.growth_rates['medium_fast'],
    },
    {
        'name': 'Branched_two_stage',
        'length': 2,
        'special_evo': True,
        'id': [],
        'branched': True,
        'stats': {
            1: (300, 30, fc.beta_standard),
            2: (150, 30, fc.beta_standard),
            },
        'catch_rate': {
            1: 190,
            2: 70,
            },
        'exp_yield': fc.two_stage_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_fast'],
    },
    {
        'name': 'Branched_three_stage',
        'length': 3,
        'special_evo': True,
        'id': [],
        'branched': True,
        'stats': {
            1: (290, 30, fc.beta_standard),
            2: (70, 30, fc.beta_standard),
            3: (70, 40, fc.beta_standard),
            },
        'catch_rate': {
            1: 255,
            2: 120,
            3: 45,
            },
        'exp_yield': fc.three_stage_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_slow'],
    },
    {
        'name': 'Ditto',
        'used': True,  # set to False to disable
        'length': 1,
        'chance': 0.6,
        'id': (132,),
        'stats': {
            1: (275, 40, fc.beta_tight),
            },
        'catch_rate': {
            1: 35,
            },
        'exp_yield': {
            1: (4, 0.2),
            },
        'type': 0,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_fast'],
    },
    {
        'name': 'Unown',
        'used': True,  # set to False to disable
        'length': 1,
        'chance': 0.6,
        'id': (201,),
        'stats': {
            1: (290, 85, fc.beta_tight),
            },
        'catch_rate': {
            1: 225,
            },
        'exp_yield': {
            1: (10.6, 0.15),
            },
        'egg_cycles': 40,
        'growth_rate': c.growth_rates['medium_fast'],
    },
    {
        'name': 'Smeargle',
        'used': True,  # set to False to disable
        'length': 1,
        'chance': 0.6,
        'id': (235,),
        'stats': {
            1: (230, 70, fc.beta_standard),
            },
        'catch_rate': {
            1: 45,
            },
        'exp_yield': {
            1: (23, 0.33),
            },
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['fast'],
    },
    {
        'name': 'Wobbuffet',
        'used': True,  # set to False to disable
        'length': 1,
        'chance': 0.6,
        'id': (202,),
        'stats': {
            1: (360, 80, fc.beta_tight),
            },
        'catch_rate': {
            1: 45,
            },
        'exp_yield': {
            1: (0, 0.437),
            },
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_fast'],
    },
    {
        'name': 'Three_stage_bugs',
        'used': True,  # set to False to disable
        'length': 3,
        'id': (10, 13),
        'stats': {
            1: (192, 16, fc.beta_tight),
            2: (20, 10, fc.beta_standard),
            3: (142, 16, fc.beta_tight),
            },
        'catch_rate': {
            1: 255,
            2: 120,
            3: 45,
            },
        'exp_yield': {
            1: (14,0.2),
            2: (3,0.33),
            3: (31,0.33),
            },
        'egg_cycles': 15,
        'growth_rate': c.growth_rates['medium_fast'],
    },
]

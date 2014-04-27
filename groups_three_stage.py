#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import constants as fc
from pygsc import constants as c

groups_three_stage = [
    {
        'name': 'Three_stage_strong_special_evo',
        'used': True,  # set to False to disable
        'length': 3,
        'amount': (2, 4),
        'special_evo': True,
        'stats': {
            1: (300, 20, fc.beta_standard),
            2: (80, 20, fc.beta_standard),
            3: (85, 30, fc.beta_standard),
            },
        'catch_rate': {
            1: (235, 255),
            2: (120, 170),
            3: (45, 75),
            },
        'exp_yield': fc.three_stage_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_slow'],
    },
    {
        'name': 'Three_stage_weak_special_evo',
        'used': True,  # set to False to disable
        'length': 3,
        'amount': (2, 4),
        'special_evo': True,
        'stats': {
            1: (240, 60, fc.beta_tight),
            2: (80, 20, fc.beta_standard),
            3: (85, 30, fc.beta_standard),
            },
        'catch_rate': {
            1: 255,
            2: (150, 190),
            3: (50, 75),
            },
        'exp_yield': fc.three_stage_exp_yield,
        'egg_cycles': 10,
        'growth_rate': c.growth_rates['medium_slow'],
    },
    {
        'name': 'Pseudo_legendary',
        'used': True,  # set to False to disable
        'length': 3,
        'amount': (2, 2),  # always 2 pseudo-legendary families
        'stats': {
            1: (296, 8, fc.beta_standard),
            2: (106, 8, fc.beta_standard),
            3: (186, 8, fc.beta_standard),
            },
        'catch_rate': {
            1: 45,
            2: 45,
            3: 45,
            },
        'exp_yield': {
            1: (1, 0.22),
            2: (-18, 0.39),
            3: (-154, 0.62),
            },
        'egg_cycles': 40,
        'growth_rate': c.growth_rates['slow'],
    },
    {
        'name': 'Three_stage_weak',
        'used': True,  # set to False to disable
        'length': 3,
        'amount': (2, 4),
        'stats': {
            1: (240, 60, fc.beta_tight),
            2: (80, 20, fc.beta_standard),
            3: (85, 30, fc.beta_standard),
            },
        'catch_rate': {
            1: (235, 255),
            2: 120,
            3: 45,
            },
        'exp_yield': fc.three_stage_exp_yield,
        'egg_cycles': (15, 20),
        'growth_rate': c.growth_rates['medium_slow'],
    },
    {
        'name': 'Average_three_stage',
        'used': True,  # set to False to disable
        'default': True,  # all unassigned one-stage Pokemon go here
        'length': 3,
        'stats': {
            1: (295, 25, fc.beta_tight),
            2: (70, 20, fc.beta_standard),
            3: (80, 20, fc.beta_standard),
            },
        'catch_rate': {
            1: (235, 255),
            2: (95, 150),
            3: 45,
            },
        'exp_yield': fc.three_stage_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_slow'],
    },

]
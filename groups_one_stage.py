#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import constants as fc
from pygsc import constants as c

groups_one_stage = [
    {
        'name': 'Strong_one_stage',
        'used': True,  # set to False to disable
        'length': 1,
        'amount': (9, 12),
        'stats': {
            1: (460, 80, fc.beta_right_tilted),
            },
        'catch_rate': {
            1: 45,
            },
        'exp_yield': fc.one_stage_exp_yield,
        'egg_cycles': (20, 35),
        'growth_rate': c.growth_rates['slow'],
    },
    {
        'name': 'Weak_one_stage',
        'used': True,  # set to False to disable
        'length': 1,
        'amount': (2, 4),
        'stats': {
            1: (315, 60, fc.beta_standard),
            },
        'catch_rate': {
            1: (45, 90),
            },
        'exp_yield': fc.one_stage_exp_yield,
        'egg_cycles': 20,
        'growth_rate': (
            c.growth_rates['medium_fast'],
            c.growth_rates['fast'],
            ),
    },
    {
        'name': 'Average_one_stage',
        'used': True,  # set to False to disable
        'default': True,  # all unassigned one-stage Pokemon go here
        'length': 1,
        'stats': {
            1: (375, 90, fc.beta_standard),
            },
        'catch_rate': {
            1: (45, 75),
            },
        'exp_yield': fc.one_stage_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_fast'],
    },
]


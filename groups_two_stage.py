#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import constants as fc
from pygsc import constants as c

groups_two_stage = [
    {
        'name': 'Strong_two_stage_special_evo',
        'used': True,  # set to False to disable
        'length': 2,
        'amount': (2, 4),
        'special_evo': True,
        'stats': {
            1: (300, 50, fc.beta_standard),
            2: (175, 25, fc.beta_tight),
            },
        'catch_rate': {
            1: (80, 120),
            2: (45, 65),
            },
        'exp_yield': fc.two_stage_strong_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['slow'],
    },
    {
        'name': 'Strong_two_stage_weak_first_stage',
        'used': True,  # set to False to disable
        'length': 2,
        'amount': (1, 2),
        'stats': {
            1: (350, 50, fc.beta_tight),
            2: (100, 60, fc.beta_tight),
            },
        'catch_rate': {
            1: (45, 180),
            2: (45, 65),
            },
        'exp_yield': fc.two_stage_strong_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['slow'],
    },
    {
        'name': 'Average_two_stage_special_evo',
        'used': True,  # set to False to disable
        'length': 2,
        'amount': (1, 2),
        'stats': {
            1: (280, 40, fc.beta_standard),
            2: (130, 50, fc.beta_standard),
            },
        'catch_rate': {
            1: (190, 255),
            2: (60, 90),
            },
        'exp_yield': fc.two_stage_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_fast'],
    },
    {
        'name': 'Strong_two_stage_weak_first_stage',
        'used': True,  # set to False to disable
        'length': 2,
        'amount': (1, 3),
        'stats': {
            1: (295, 55, fc.beta_standard),
            2: (170, 30, fc.beta_tight),
            },
        'catch_rate': {
            1: (80, 120),
            2: (45, 65),
            },
        'exp_yield': fc.two_stage_strong_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['slow'],
    },
    {
        'name': 'Strong_two_stage',
        'used': True,  # set to False to disable
        'length': 2,
        'amount': (2, 3),
        'stats': {
            1: (345, 55, fc.beta_tight),
            2: (105, 55, fc.beta_tight),
            },
        'catch_rate': {
            1: (45, 180),
            2: (45, 65),
            },
        'exp_yield': fc.two_stage_strong_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['slow'],
    },
    {
        'name': 'Average_two_stage_weak_first_stage',
        'used': True,  # set to False to disable
        'length': 2,
        'amount': (13, 17),
        'stats': {
            1: (280, 40, fc.beta_standard),
            2: (140, 40, fc.beta_standard),
            },
        'catch_rate': {
            1: (190, 255),
            2: (60, 90),
            },
        'exp_yield': fc.two_stage_exp_yield,
        'egg_cycles': 20,
        'growth_rate': c.growth_rates['medium_fast'],
    },
    {
        'name': 'Average_two_stage_terrible_first_stage',
        'used': True,  # set to False to disable
        'length': 2,
        'amount': (5, 8),
        'stats': {
            1: (230, 50, fc.beta_standard),
            2: (140, 60, fc.beta_tight),
            },
        'catch_rate': {
            1: (225, 255),
            2: (75, 120),
            },
        'exp_yield': fc.two_stage_exp_yield,
        'egg_cycles': (15, 25),
        'growth_rate': c.growth_rates['medium_fast'],
    },
    {
        'name': 'Magikarp_like',
        'used': True,  # set to False to disable
        'length': 2,
        'amount': (1, 2),
        'stats': {
            1: (185, 30, fc.beta_standard),
            2: (330, 20, fc.beta_standard),
            },
        'catch_rate': {
            1: 255,
            2: 45,
            },
        'exp_yield': {
            1: (6.6, 0.067),
            2: (0, 0.4),
            },
        'egg_cycles': 5,
        'growth_rate': c.growth_rates['slow'],
    },
    {
        'name': 'Average_two_stage',
        'used': True,  # set to False to disable
        'default': True,  # all unassigned one-stage Pokemon go here
        'length': 2,
        'stats': {
            1: (320, 60, fc.beta_left_tilted),
            2: (80, 40, fc.beta_standard),
            },
        'catch_rate': {
            1: (120, 225),
            2: (45, 90),
            },
        'exp_yield': fc.two_stage_exp_yield,
        'egg_cycles': (20, 30),
        'growth_rate': c.growth_rates['medium_fast'],
    },
]
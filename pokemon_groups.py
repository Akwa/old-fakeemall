#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import constants as fc
from groups_special import groups_special
from groups_three_stage import groups_three_stage
from groups_two_stage import groups_two_stage
from groups_one_stage import groups_one_stage
import random

all_groups = (groups_special, groups_three_stage, groups_two_stage, groups_one_stage)

branched_groups = {}
priority_groups = []
other_groups = []

default_groups = []

""" Group container dict """
groups = {}

for group_type in all_groups:
    for group in group_type:
        len_groups = len(groups)
        group['#'] = len_groups
        groups[len_groups] = group
        if 'branched' in group:
            branched_groups[group['length']] = group
        elif 'id' in group:
            # Convert from 1-based to 0-based indexing
            group['id'] = [i - 1 for i in group['id']]
            priority_groups.append(group)
        elif 'default' in group:
            default_groups.append(group)
        else:
            other_groups.append(group)
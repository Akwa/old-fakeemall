#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from pygsc import constants as c
import constants as fc
import settings as fs
import pokemon_groups as g
import random
r = random.random

def fake_pokemon(pokemon):
    randomize_groups(pokemon)
    randomize_types(pokemon)

def randomize_types(pokemon):
    for i in range(c.max_pokemon):
        pk = pokemon[i]

def randomize_groups(pokemon):
    prim_families = get_primary(pokemon)
    assign_branched_to_groups(g.groups, pokemon)
    """
    Priority groups
    """
    for group in g.priority_groups:
        if no_chance(group):
            continue
        ids = group['id']
        number = group['#']
        for i in ids:
            pk = pokemon[i]
            pk.group = number
            inherit_group(pokemon, i, number)
            prim_families[pk.family_len].remove(i)
    """
    Branched groups
    """
    for group in g.branched_groups.values():
        ids = group['id']
        number = group['#']
        for i in ids:
            pk = pokemon[i]
            if hasattr(pk, 'group'):
                continue
            pk.group = number
            inherit_group(pokemon, i, number)
            prim_families[pk.family_len].remove(i)
    """
    Other groups
    """
    for group in g.other_groups:
        if no_chance(group):
            continue
        number = group['#']
        for n in range(random.randint(*group['amount'])):
            i = prim_families[group['length']].pop()
            pokemon[i].group = number
            inherit_group(pokemon, i, number)
    """
    Default groups
    """
    for group in g.default_groups:
        number = group['#']
        for i in prim_families[group['length']]:
            pokemon[i].group = number
            inherit_group(pokemon, i, number)

    for i in range(c.max_pokemon):
        print('%10s %40s' % (pokemon[i].name, g.groups[pokemon[i].group]['name']))

def no_chance(group):
    if 'chance' in group:
        if r() > group['chance']:
           return True
    return False

def inherit_group(pokemon, i, number):
    for *x, j in pokemon[i].evos:
        pokemon[j].group = number
        inherit_group(pokemon, j, number)

def get_primary(pokemon):
    one, two, three = [], [], []
    for i in pokemon.primary_pokemon:
        family_len = pokemon[i].family_len
        {1: one, 2: two, 3: three}[family_len].append(i)
    random.shuffle(one)
    random.shuffle(two)
    random.shuffle(three)
    return {
        1: one,
        2: two,
        3: three,
        }

def assign_branched_to_groups(groups, pokemon):
    for i in pokemon.primary_pokemon:
        pk = pokemon[i]
        if pk.branched_family:
            g.branched_groups[pk.family_len]['id'].append(i)
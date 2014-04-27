#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import settings as s

from string import (ascii_lowercase,
                    ascii_uppercase,
                    digits
                    )

characters = ''.join((ascii_lowercase, ascii_uppercase, digits))

def generate_seed():
    if s.random_seed is None:
        return ''.join(random.choice(characters) for i in range(32))
    return s.random_seed
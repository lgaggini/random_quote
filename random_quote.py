# -*- coding: utf-8 -*-
"""
Random Quote Plugin For Pelican
==================================

Adds random quote from configured file
to Pelican on generation
"""

import random

from pelican import signals

def add_random_quote(generator):
    if 'RANDOM_QUOTE' in generator.settings.keys():
        try:
            generator.settings['QUOTE'] = (random.choice(open(generator.settings['RANDOM_QUOTE']).readlines())).decode('utf-8')
        except IOError:
            generator.settings['QUOTE'] = "Missing quote file: " + generator.settings['RANDOM_QUOTE']
    
def register():
    signals.initialized.connect(add_random_quote)

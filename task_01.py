#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """ this gets two inputs and returns a string and displays winks.

    Args:
         wink (mixed): this will get repeated
         numwick (int): number of times to repeat the 'nudge' default value of 2

    Returns:
          str: Both arguments possibly repeated following a question.

    Examples:
          >>>'Know what I mean? (number of)winks, nudges.'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr

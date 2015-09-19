#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining a function with three parameters."""

def too_many_kittens(kittens, litterboxes, catfood):
    """Three Parameters.
    Args:
        kittens(mixed): number of kittens
        litterboxes(int): number of availabe litterboxes
        catfood(boolean): is there catfood or not
        
    Returns:
        True or False on whether we have too many kittens,

    Examples:
        >>>too_many_kittens(12, 12, False)
        True
    """
 return not (litterboxes >= kittens and catfood)

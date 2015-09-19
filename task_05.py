#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some pretty crazy math."""


def defaults(my_required, my_optional=True):
    """Declares two parameters.

    Args:
        my_required: does not contain any default
        my_optional: contains default
    Returns:
        boolean value: Whether the two parameters are the same
    Examples
    >>> defaults(True)
    True
    >>> defaults (True,False)
    False
    """
    return my_optional is my_required

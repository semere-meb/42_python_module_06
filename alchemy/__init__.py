#! /usr/bin/env python3


from .elements import create_water, create_fire, create_earth, create_air
from .potions import strength_potion

__all__ = [
    "create_fire",
    "create_water",
    "create_earth",
    "create_air",
    "strength_potion",
]

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

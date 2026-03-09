#! /usr/bin/env python3


from alchemy.elements import create_earth, \
    create_water, \
    create_air, \
    create_fire


fire = create_fire()
water = create_water()
air = create_air()
earth = create_earth()


def healing_potion() -> str:
    return f"Healing potion brewed with {fire} and {water}"


def strength_potion() -> str:
    return f"Strength potion brewed with {earth} and {fire}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {air} and {water}"


def wisdom_potion() -> str:
    res = fire + water + air + earth
    return f"Wisdom potion brwed with all elements: {res}"

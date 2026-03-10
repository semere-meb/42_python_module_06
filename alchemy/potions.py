from alchemy.elements import create_earth, create_air, create_fire
from .elements import create_water as water


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {create_air()} and {water()}"


def wisdom_potion() -> str:
    all_result = create_fire() + ' ' + \
        water() + ' ' + \
        create_air() + ' ' + \
        create_earth()

    return f"Wisdom potion brwed with all elements: {all_result}"

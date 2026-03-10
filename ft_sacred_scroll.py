#! /usr/bin/env python3


import alchemy


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")
    print("alchemy.elements.create_fire(): ", alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): ", alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): ", alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): ", alchemy.elements.create_air())

    print("\nTesting direct module access (controlled by __init__.py):")
    print("alchemy.elements.create_fire():", alchemy.create_fire())
    print("alchemy.elements.create_water():", alchemy.create_water())

    try:
        print("alchemy.elements.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    try:
        print("alchemy.elements.create_air(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version", alchemy.__version__)
    print("Author", alchemy.__author__)


if __name__ == "__main__":
    main()

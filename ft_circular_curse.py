#! /bin/usr/env python3


from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    test = "fire air"
    print(f'Validate ingredients("{test}"): {validate_ingredients(test)}')
    test = "dragon scales"
    print(f'Validate ingredients("{test}"): {validate_ingredients(test)}')

    print("\nTesting spell recording with validation:")
    test = ("Fireball", "fire air")
    print(f"record_spell{test}: {record_spell(*test)}")
    test = ("Dark Magic", "shadow")
    print(f"record_spell{test}: {record_spell(*test)}")

    print("\nTesting late import technique:")
    test = ("Lightning", "air")
    print(f"record_spell{test}: {record_spell(*test)}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()

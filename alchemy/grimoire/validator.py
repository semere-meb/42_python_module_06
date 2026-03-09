# from .spellbook import record_spell  # noqa: F401


__valid_ingredients = [
    "fire",
    "water",
    "earth",
    "air",
]


def validate_ingredients(ingredients: str) -> str:
    from .spellbook import record_spell  # noqa: F401, F811

    is_valid = any([x for x in __valid_ingredients if x in ingredients])
    return f"{ingredients} - {'VALID' if is_valid else 'INVALID'}"

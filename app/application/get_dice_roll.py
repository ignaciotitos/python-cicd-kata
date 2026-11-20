import secrets


def get_dice_roll() -> int:
    return secrets.randbelow(6) + 2

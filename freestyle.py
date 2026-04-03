#!/usr/bin/env python3
"""Randomly pick a beverage from a Coca-Cola Freestyle machine."""

import argparse
import random
from dataclasses import dataclass


@dataclass
class Beverage:
    name: str
    brand: str
    flavor: str
    diet: bool  # True = diet or zero sugar / low calorie


BEVERAGES = [
    # Coca-Cola family
    Beverage("Coca-Cola", "Coca-Cola", "Original", diet=False),
    Beverage("Coca-Cola Cherry", "Coca-Cola", "Cherry", diet=False),
    Beverage("Coca-Cola Vanilla", "Coca-Cola", "Vanilla", diet=False),
    Beverage("Coca-Cola Orange Vanilla", "Coca-Cola", "Orange Vanilla", diet=False),
    Beverage("Coca-Cola Zero Sugar", "Coca-Cola", "Original", diet=True),
    Beverage("Coca-Cola Zero Sugar Cherry", "Coca-Cola", "Cherry", diet=True),
    Beverage("Coca-Cola Zero Sugar Vanilla", "Coca-Cola", "Vanilla", diet=True),
    Beverage("Diet Coke", "Diet Coke", "Original", diet=True),
    Beverage("Diet Coke Feisty Cherry", "Diet Coke", "Feisty Cherry", diet=True),
    Beverage("Diet Coke Twisted Mango", "Diet Coke", "Twisted Mango", diet=True),
    Beverage("Diet Coke Ginger Lime", "Diet Coke", "Ginger Lime", diet=True),
    # Sprite family
    Beverage("Sprite", "Sprite", "Original", diet=False),
    Beverage("Sprite Cherry", "Sprite", "Cherry", diet=False),
    Beverage("Sprite Tropical Mix", "Sprite", "Tropical Mix", diet=False),
    Beverage("Sprite Zero Sugar", "Sprite", "Original", diet=True),
    Beverage("Sprite Zero Sugar Cherry", "Sprite", "Cherry", diet=True),
    # Fanta family
    Beverage("Fanta Orange", "Fanta", "Orange", diet=False),
    Beverage("Fanta Strawberry", "Fanta", "Strawberry", diet=False),
    Beverage("Fanta Grape", "Fanta", "Grape", diet=False),
    Beverage("Fanta Pineapple", "Fanta", "Pineapple", diet=False),
    Beverage("Fanta Zero Orange", "Fanta", "Orange", diet=True),
    # Barq's
    Beverage("Barq's Root Beer", "Barq's", "Root Beer", diet=False),
    Beverage("Diet Barq's Root Beer", "Barq's", "Root Beer", diet=True),
    # Pibb
    Beverage("Pibb Xtra", "Pibb", "Original", diet=False),
    Beverage("Pibb Zero", "Pibb", "Original", diet=True),
    # Mello Yello
    Beverage("Mello Yello", "Mello Yello", "Original", diet=False),
    Beverage("Mello Yello Zero", "Mello Yello", "Original", diet=True),
    # Powerade
    Beverage(
        "Powerade Mountain Berry Blast", "Powerade", "Mountain Berry Blast", diet=False
    ),
    Beverage("Powerade Fruit Punch", "Powerade", "Fruit Punch", diet=False),
    Beverage("Powerade Orange", "Powerade", "Orange", diet=False),
    Beverage("Powerade Grape", "Powerade", "Grape", diet=False),
    Beverage("Powerade Zero Berry Ice", "Powerade", "Berry Ice", diet=True),
    Beverage("Powerade Zero Fruit Punch", "Powerade", "Fruit Punch", diet=True),
    Beverage("Powerade Zero Grape", "Powerade", "Grape", diet=True),
    Beverage("Powerade Zero Orange", "Powerade", "Orange", diet=True),
    # Hi-C
    Beverage("Hi-C Orange Lavaburst", "Hi-C", "Orange", diet=False),
    Beverage("Hi-C Fruit Punch", "Hi-C", "Fruit Punch", diet=False),
    # Minute Maid
    Beverage("Minute Maid Lemonade", "Minute Maid", "Lemonade", diet=False),
    Beverage("Minute Maid Pink Lemonade", "Minute Maid", "Pink Lemonade", diet=False),
    Beverage("Minute Maid Fruit Punch", "Minute Maid", "Fruit Punch", diet=False),
    Beverage("Minute Maid Light Lemonade", "Minute Maid", "Lemonade", diet=True),
    # Gold Peak Tea
    Beverage("Gold Peak Sweet Tea", "Gold Peak", "Sweet Tea", diet=False),
    Beverage("Gold Peak Unsweetened Tea", "Gold Peak", "Unsweetened Tea", diet=True),
    Beverage("Gold Peak Peach Tea", "Gold Peak", "Peach Tea", diet=False),
    Beverage("Gold Peak Lemon Tea", "Gold Peak", "Lemon Tea", diet=False),
    Beverage("Gold Peak Zero Sugar Sweet Tea", "Gold Peak", "Sweet Tea", diet=True),
    # FUZE Tea
    Beverage("FUZE Raspberry Tea", "FUZE", "Raspberry Tea", diet=False),
    Beverage("FUZE Peach Tea", "FUZE", "Peach Tea", diet=False),
    # Seagram's
    Beverage("Seagram's Ginger Ale", "Seagram's", "Ginger Ale", diet=False),
    Beverage("Seagram's Diet Ginger Ale", "Seagram's", "Ginger Ale", diet=True),
    # Dasani
    Beverage("Dasani Water", "Dasani", "Plain", diet=True),
    Beverage("Dasani Lemon", "Dasani", "Lemon", diet=True),
    Beverage("Dasani Strawberry", "Dasani", "Strawberry", diet=True),
    Beverage("Dasani Apple", "Dasani", "Apple", diet=True),
]


def main():
    parser = argparse.ArgumentParser(
        description="Pick a random Coca-Cola Freestyle beverage."
    )
    parser.add_argument(
        "--diet",
        action="store_true",
        help="Pick only from diet / zero sugar / low calorie options.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available beverages and exit.",
    )
    args = parser.parse_args()

    pool = [b for b in BEVERAGES if not args.diet or b.diet]

    if args.list:
        label = "Diet/Low Calorie" if args.diet else "All"
        print(f"{label} Beverages ({len(pool)}):")
        for b in sorted(pool, key=lambda b: b.name):
            tag = " [diet]" if b.diet else ""
            print(f"  {b.name}{tag}")
        return

    pick = random.choice(pool)
    tag = " (diet/low calorie)" if pick.diet else ""
    print(f"{pick.name}{tag}")


if __name__ == "__main__":
    main()

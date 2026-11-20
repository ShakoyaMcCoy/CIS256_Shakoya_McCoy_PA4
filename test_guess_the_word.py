
# Shakoya McCoy
# CIS256 Fall 2026
# Programming Assignment 4

import random

car_brands = ["Toyota", "Lexus", "Honda", "Mazda", "Tesla"]


# Check that a random car brand comes from the list.
def test_random_brand():
    chosen_brand = random.choice(car_brands)
    assert chosen_brand in car_brands


# Check if the correct letters are recognized.
def test_correct_guess():
    chosen_brand = "Toyota"
    assert "t" in chosen_brand.lower()
    assert "o" in chosen_brand.lower()


# Check if incorrect letters are recognized.
def test_incorrect_guess():
    chosen_brand = "Toyota"
    assert "z" not in chosen_brand.lower()

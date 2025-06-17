import pytest
from conversions import convert

# test each conversion

def test_temperature_conversions():
    assert round(convert("Fahrenheit", "Celsius", 32), 2) == 0
    assert round(convert("Celsius", "Fahrenheit", 0), 2) == 32
    assert round(convert("Celsius", "Kelvin", 100), 2) == 373.15
    assert round(convert("Kelvin", "Celsius", 273.15), 2) == 0

def test_distance_conversions():
    assert round(convert("Miles", "Kilometers", 1), 5) == 1.60934
    assert round(convert("Feet", "Meters", 1), 5) == 0.3048
    assert round(convert("Inches", "Meters", 1), 5) == 0.0254

def test_weight_conversions():
    assert round(convert("Pounds", "Kilograms", 1), 5) == 0.45359
    assert round(convert("Ounces", "Grams", 1), 5) == 28.3495
    assert round(convert("Tons", "Pounds", 1), 2) == 2000

# test same type conversion case

def test_same_unit_returns_input():
    assert convert("Kilograms", "Kilograms", 100) == 100

# test invalid conversion case

def test_invalid_conversion():
    assert convert("Celsius", "Miles", 100) == "Invalid Conversion"
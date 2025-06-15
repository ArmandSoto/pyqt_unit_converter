def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def celsius_to_kelvin(c): return c + 273.15
def kelvin_to_celsius(k): return k - 273.15
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32

conversions = {
    ("Fahrenheit", "Celsius"): fahrenheit_to_celsius,
    ("Celsius", "Fahrenheit"): celsius_to_fahrenheit,
    ("Celsius", "Kelvin"): celsius_to_kelvin,
    ("Kelvin", "Celsius"): kelvin_to_celsius,
    ("Fahrenheit", "Kelvin"): fahrenheit_to_kelvin,
    ("Kelvin", "Fahrenheit"): kelvin_to_fahrenheit,
}

def convert(from_unit, to_unit, value):
    try:
        return conversions[(from_unit, to_unit)](value)
    except KeyError:
        return value
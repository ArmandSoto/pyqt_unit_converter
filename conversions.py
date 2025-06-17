
# Temperatures
def fahrenheit_to_celsius(f): return (f - 32) * 5/9
def celsius_to_fahrenheit(c): return (c * 9/5) + 32
def celsius_to_kelvin(c): return c + 273.15
def kelvin_to_celsius(k): return k - 273.15
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32

# Distance
def inches_to_feet(i): return i/12
def inches_to_miles(i): return i / 63360
def inches_to_meters(i): return i * 0.0254
def inches_to_kilometers(i): return i * 0.0000254

def feet_to_inches(f): return f * 12
def feet_to_miles(f): return f / 5280
def feet_to_meters(f): return f * 0.3048
def feet_to_kilometers(f): f * 0.0003048

def miles_to_inches(m): return m * 633360
def miles_to_feet(m): return m * 5280
def miles_to_meters(m): return m * 1609.34
def miles_to_kilometers(m): return m * 1.60934

def meters_to_inches(m): return m / 0.0254
def meters_to_feet(m): return m / 0.3048
def meters_to_miles(m): return m / 1609.34
def meters_to_kilometers(m): return m / 1000

def kilometers_to_inches(k): return k * 39370.1
def kilometers_to_feet(k): return k * 3280.84
def kilometers_to_miles(k): return k * 1.60934
def kilometers_to_meters(k): return k * 1000

# Weight
def pounds_to_kilograms(p): return p * 0.453592
def pounds_to_ounces(p): return p * 16
def pounds_to_grams(p): return p * 453.592
def pounds_to_tons(p): return p / 2000

def kilograms_to_pounds(k): return k / 0.453592
def kilograms_to_ounces(k): return k * 35.274
def kilograms_to_grams(k): return k * 1000
def kilograms_to_tons(k): return k / 907.18474

def ounces_to_pounds(oz): return oz / 16
def ounces_to_kilograms(oz): return oz * 0.0283495
def ounces_to_grams(oz): return oz * 28.3495
def ounces_to_tons(oz): return oz / 32000

def grams_to_pounds(g): return g / 453.592
def grams_to_kilograms(g): return g / 1000
def grams_to_ounces(g): return g / 28.3495
def grams_to_tons(g): return g / 907184.74

def tons_to_pounds(t): return t * 2000
def tons_to_kilograms(t): return t * 907.18474
def tons_to_ounces(t): return t * 32000
def tons_to_grams(t): return t * 907184.74

conversions = {
    ("Fahrenheit", "Celsius"): fahrenheit_to_celsius,
    ("Fahrenheit", "Kelvin"): fahrenheit_to_kelvin,
    ("Celsius", "Fahrenheit"): celsius_to_fahrenheit,
    ("Celsius", "Kelvin"): celsius_to_kelvin,
    ("Kelvin", "Celsius"): kelvin_to_celsius,
    ("Kelvin", "Fahrenheit"): kelvin_to_fahrenheit,
    ("Inches", "Feet"): inches_to_feet,
    ("Inches", "Miles"): inches_to_miles,
    ("Inches", "Meters"): inches_to_meters,
    ("Inches", "kilometers"): inches_to_kilometers,
    ("Feet", "Inches"): feet_to_inches,
    ("Feet", "Miles"): feet_to_miles,
    ("Feet", "Meters"): feet_to_meters,
    ("Feet", "Kilometers"): feet_to_meters,
    ("Miles", "Inches"): miles_to_inches,
    ("Miles", "Feet"): miles_to_feet,
    ("Miles", "Meters"): miles_to_meters,
    ("Miles", "Kilometers"): miles_to_kilometers,
    ("Meters", "Inches"): meters_to_inches,
    ("Meters", "Feet"): meters_to_feet,
    ("Meters", "Miles"): meters_to_miles,
    ("Meters", "Kilometers"): meters_to_kilometers,
    ("Kilometers", "Inches"): kilometers_to_inches,
    ("Kilometers", "Feet"): kilometers_to_feet,
    ("Kilometers", "Miles"): kilometers_to_miles,
    ("Kilometers", "Inches"): kilometers_to_meters,
    ("Pounds", "Kilograms"): pounds_to_kilograms,
    ("Pounds", "Ounces"): pounds_to_ounces,
    ("Pounds", "Grams"): pounds_to_grams,
    ("Pounds", "Tons"): pounds_to_tons,
    ("Kilograms", "Pounds"): kilograms_to_pounds,
    ("Kilograms", "Ouces"): kilograms_to_ounces,
    ("Kilograms", "Grams"): kilograms_to_grams,
    ("Kilograms", "Tons"): kilograms_to_tons,
    ("Ounces", "Pounds"): ounces_to_pounds,
    ("Ounces", "Kilograms"): ounces_to_kilograms,
    ("Ounces", "Grams"): ounces_to_grams,
    ("Ounces", "Tons"): ounces_to_tons,
    ("Grams", "Pounds"): grams_to_pounds,
    ("Grams", "Kilograms"): grams_to_kilograms,
    ("Grams", "Ounces"): grams_to_ounces,
    ("Grams", "Tons"): grams_to_tons,
    ("Tons", "Pounds"): tons_to_pounds,
    ("Tons", "Kilograms"): tons_to_kilograms,
    ("Tons", "Ounces"): tons_to_ounces,
    ("Tons", "Grams"): tons_to_grams,

}

def convert(from_unit, to_unit, value):
    if (from_unit == to_unit):
        return value
    try:
        return conversions[(from_unit, to_unit)](value)
    except KeyError:
        return "Invalid Conversion"
import pint

def fetch_units():
    ureg = pint.UnitRegistry()
    units = [str(unit) for unit in ureg]
    return units

def get_compatible_units(unit):
    ureg = pint.UnitRegistry()
    try:
        input_quantity = ureg(unit)
        base_unit = input_quantity.dimensionality
        compatible_units = [str(u) for u in ureg if ureg(u).dimensionality == base_unit]
        return compatible_units
    except Exception as e:
        print(f"Error fetching compatible units: {e}")
        return []

def convert_units(value, from_unit, to_unit):
    ureg = pint.UnitRegistry()
    from_quantity = value * ureg(from_unit)
    to_quantity = from_quantity.to(ureg(to_unit))
    return to_quantity.magnitude

def main():
    print("Welcome to the Unit Converter")
    units = fetch_units()
    if units:
        print("Available units:", ', '.join(units))
    else:
        print("Failed to fetch units.")
        return

    value = float(input("Enter the value to convert: "))
    from_unit = input("Enter the unit to convert from: ").strip().lower()

    compatible_units = get_compatible_units(from_unit)
    if compatible_units:
        print("You can convert to the following units:", ', '.join(compatible_units))
    else:
        print("No compatible units found.")

    to_unit = input("Enter the unit to convert to: ").strip().lower()

    if to_unit not in compatible_units:
        print("Invalid conversion unit entered.")
        return

    try:
        result = convert_units(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    except Exception as e:
        print(f"Failed to perform conversion: {e}")

if __name__ == "__main__":
    main()




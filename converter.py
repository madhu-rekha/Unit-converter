def convert_length(value, from_unit, to_unit):
    """Convert between length units."""
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701,
    }
    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[to_unit] / length_units[from_unit])
    else:
        print("Invalid length units.")
        return None

def convert_weight(value, from_unit, to_unit):
    """Convert between weight units."""
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "pounds": 2.20462,
        "ounces": 35.274,
    }
    if from_unit in weight_units and to_unit in weight_units:
        return value * (weight_units[to_unit] / weight_units[from_unit])
    else:
        print("Invalid weight units.")
        return None

def convert_temperature(value, from_unit, to_unit):
    """Convert between temperature units."""
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    else:
        print("Invalid temperature units.")
        return None

def main():
    print("Unit Converter")
    regions = {
        "1": "Metric (meters, kilograms, Celsius)",
        "2": "Imperial (miles, pounds, Fahrenheit)"
    }
    
    print("Choose your region:")
    for key, value in regions.items():
        print(f"{key}. {value}")
    
    region_choice = input("Enter the number of your choice: ")
    if region_choice == "1":
        preferred_length = ["meters", "kilometers"]
        preferred_weight = ["kilograms", "grams"]
        preferred_temp = ["Celsius", "Kelvin"]
    elif region_choice == "2":
        preferred_length = ["miles", "feet", "inches"]
        preferred_weight = ["pounds", "ounces"]
        preferred_temp = ["Fahrenheit"]
    else:
        print("Invalid choice. Defaulting to Metric.")
        preferred_length = ["meters", "kilometers"]
        preferred_weight = ["kilograms", "grams"]
        preferred_temp = ["Celsius", "Kelvin"]
    
    while True:
        print("\nChoose a conversion type:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(f"Available units: {preferred_length}")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input(f"Enter value in {from_unit}: "))
            result = convert_length(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} = {result:.2f} {to_unit}")
        elif choice == "2":
            print(f"Available units: {preferred_weight}")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input(f"Enter value in {from_unit}: "))
            result = convert_weight(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} = {result:.2f} {to_unit}")
        elif choice == "3":
            print(f"Available units: {preferred_temp}")
            from_unit = input("Convert from: ").capitalize()
            to_unit = input("Convert to: ").capitalize()
            value = float(input(f"Enter value in {from_unit}: "))
            result = convert_temperature(value, from_unit, to_unit)
            if result is not None:
                print(f"{value} {from_unit} = {result:.2f} {to_unit}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

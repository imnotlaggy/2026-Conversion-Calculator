# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration) :
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
- Please choose a conversion type (distance/time/mass)
- This program will show the converted source of measurement to your chosen amount
- The program will divide down for a larger source of measurement and multiply up for a smaller source of measurement
- Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit
- To exit the program, please type 'xxx'
  ''')




# Ask Users For Conversion Type (distance / time / mass)
def get_conversion_type():

    while True:
        response = input("Please enter the conversion type: ")

        # check for the exit code
        if response == "xxx":
            return response

        # check for distance conversion
        elif response in [ 'distance', 'Distance', 'DISTANCE', 'd', 'D', 'LENGTH', 'l', 'L', 'Length', 'length']:
            return "distance"

        # check for time conversion
        elif response in ['time', 'Time', 'T', 't', 'TIME']:
            return "time"

        # check for mass conversion
        elif response in ["mass", 'Mass', 'm', 'M', 'MASS', 'weight', 'Weight', 'WEIGHT', 'W', 'w']:
            return "mass"

        # if the response is invalid output an error
        else:
            print("Please enter a valid conversion type to continue.")


# Ask user for a valid number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero.\n"

    while True:

        # Exit code
        response = input(question)
        if response == "xxx":
            return "xxx"

        try:
            # ask the user for the number
            response = float(response)

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Convert Valid Units To The Correct Name
def unit_names(question):

    # list of valid units
    valid_units = [
        ["mm", "mms", "MM", "MMS", "MILLIMETER", "MILLIMETRE", "MILLIMETERS", "MILLIMETRES", "millimeters", "Millimeters", "millimeter", "Millimeter", "millimetres", "Millimetres", "millimetre", "Millimetre" ],
        ["cm", "cms", "CM", "CMS", "CENTIMETER", "CENTIMETRE", "CENTIMETERS", "CENTIMETRES", "centimeters", "Centimeters", "centimeter", "Centimeter", "centimetres", "Centimetres", "centimetre", "Centimetre"],
        ["m", "M", "METERS", "METRES", "METRE", "METER", "meters", "Meters", "meter", "Meter", "metres", "Metres", "metre", "metres"],
        ["km", "KM", "KILOMETERS", "KILOMETER", "KILOMETRES", "KILOMETRE", "kilometers", "Kilometers", "kilometer", "Kilometer", "kilometres", "Kilometres", "kilometre", "Kilometre"],
        ["ms", "MS", "MILLISECONDS", "MILLISECOND", "Milliseconds", "milliseconds", "Millisecond", "millisecond"],
        ["s", "S", "SECONDS", "SECOND", "SECS", "SEC", "seconds", "Seconds", "sec", "Sec", "Secs", "secs", "Second", "second"],
        ["min", "Min", "MINS", "MIN",  "minutes", "Minutes", "minute", "Minute", "MINUTE", "MINUTES"],
        ["hrs", "HR", "hr", "Hrs", "HRS", "Hr", "hour", "Hour", "Hours", "hours", "HOURS", "HOUR"],
        ["days", "Days", "Day", "day", "DAYS", "DAY"],
        ["w", "W", "Weeks", "weeks", "week", "Week", "WEEKS", "WEEK"],
        ["years", "Y", "YEARS", "YEAR", "y", "Year", "Years", "years", "yr", "Yr", "YR", "yrs", "Yrs", "YRS"],
        ["mg", "MG", "Mg", "mgs", "Mgs", "MGS", "MILLIGRAM", "MILLIGRAMS", "Milligrams", "milligrams", "Milligram", "milligram"],
        ["g", "G", "Grams", "grams", "Gram", "gram", "GRAMS", "GRAM"],
        ["kg", "KG", "Kg", "Kgs", "kgs", "KGS", "KILOGRAMS", "KILOGRAM", "kilogram", "Kilogram", "Kilograms", "kilograms"],
        ["t", "T", "TONS", "TON", "ton", "tons", "Ton", "Tons"]

    ]

    while True:
        response = input(question)

        for item in valid_units:
            if response in item:
                return item[0]

        else:
            print("Sorry, that is not a valid unit in this program.")


# Check user has entered valid units
def unit_checker(valid_units):
    while True:
        from_unit = unit_names("Enter the unit you want to convert from: ")


        # Unit checker
        if from_unit in valid_units:
            while True:
                to_unit = unit_names("Enter the unit you want to convert to: ")

                if to_unit in valid_units:
                    return [from_unit, to_unit]

                else:
                    print(f"Sorry, converting to '{to_unit}' is not possible.")
                    break
        else:
            print(f"Sorry, '{from_unit}' is not a valid unit.")

# Main Routine Goes Here

# Calculate Conversion And Combine Them

# All Dicts

# Distance Conversion
distance_dict = {
    "mm": 1000,
    "cm": 100,
    "m": 1,
    "km": .001
}

mass_dict = {
        "mg": 1000,
        "g": 1,
        "kg": 0.001,
        "t": .000001
}

time_dict = {
        "ms": 3600 * 1000,
        "s": 3600,
        "min": 60,
        "hrs": 1,
        "weeks": 1 / (24 * 7),
        "days": 1/24,
        "years": 1/ (24 * 365 + 6 +9/60)
}


# Display instructions if requested

statement_generator("The Ultimate Conversion Calculator", "-")

want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    # Get the type of conversion from the user
    conversion_type = get_conversion_type()

    # Exit Code
    if conversion_type == "xxx":
        break

    amount = num_check("Enter the amount you want to convert: ")
    if amount == "xxx":
        break

    if conversion_type == "distance":
        from_unit, to_unit = unit_checker(distance_dict)
        if from_unit == "xxx":
            break

        # Calculate Distance
        multiply_by = distance_dict[to_unit]
        standard = amount / distance_dict[from_unit]
        answer = standard * multiply_by

    elif conversion_type == "mass":
       from_unit, to_unit = unit_checker(mass_dict)
       if from_unit == "xxx":
           break

       # Calculate Mass
       multiply_by = mass_dict[to_unit]
       standard = amount / mass_dict[from_unit]
       answer = standard * multiply_by

    elif conversion_type == "time":
        from_unit, to_unit = unit_checker(time_dict)
        if from_unit == "xxx":
            break

        # Calculate Time
        multiply_by = time_dict[to_unit]
        standard = amount / time_dict[from_unit]
        answer = standard * multiply_by

    # Answer Statement
    print(f"There are {answer} {to_unit} in {amount} {from_unit}.")

print("\nThank you for using the Conversion Calculator. :)")


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
        response = input("Please enter the conversion type: ").lower()

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


# Convert Valid Units To The Correct Name
def unit_names(question):

    # list of possible units
    possible_units = [
        ["mm", "mms", "MM", "MMS", "MILLIMETER", "MILLIMETRE", "MILLIMETERS", "MILLIMETRES", "millimeters", "Millimeters", "millimeter", "Millimeter", "millimetres", "Millimetres", "millimetre", "Millimetre" ],
        ["cm", "cms", "CM", "CMS", "CENTIMETER", "CENTIMETRE", "CENTIMETERS", "CENTIMETRES", "centimeters", "Centimeters", "centimeter", "Centimeter", "centimetres", "Centimetres", "centimetre", "Centimetre"],
        ["m", "M", "METERS", "METRES", "METRE", "METER", "meters", "Meters", "meter", "Meter", "metres", "Metres", "metre", "metres"],
        ["km", "KM", "KILOMETERS", "KILOMETER", "KILOMETRES", "KILOMETRE", "kilometers", "Kilometers", "kilometer", "Kilometer", "kilometres", "Kilometres", "kilometre", "Kilometre"],
        ["ms", "MS", "MILLISECONDS", "MILLISECOND", "Milliseconds", "milliseconds", "Millisecond", "millisecond"],
        ["s", "S", "SECONDS", "SECOND", "SECS", "SEC", "seconds", "Seconds", "sec", "Sec", "Secs", "secs", "Second", "second"],
        ["min", "Min", "MINS", "MIN",  "minutes", "Minutes", "minute", "Minute", "MINUTE", "MINUTES"],
        ["hr", "HR", "hrs", "Hrs", "HRS", "Hr", "hour", "Hour", "Hours", "hours", "HOURS", "HOUR"],
        ["d", "D", "Days", "days", "Day", "day", "DAYS", "DAY"],
        ["w", "W", "Weeks", "weeks", "week", "Week", "WEEKS", "WEEK"],
        ["y", "Y", "YEARS", "YEAR", "year", "Year", "Years", "years", "yr", "Yr", "YR", "yrs", "Yrs", "YRS"],
        ["mg", "MG", "Mg", "mgs", "Mgs", "MGS", "MILLIGRAM", "MILLIGRAMS", "Milligrams", "milligrams", "Milligram", "milligram"],
        ["g", "G", "Grams", "grams", "Gram", "gram", "GRAMS", "GRAM"],
        ["kg", "KG", "Kg", "Kgs", "kgs", "KGS", "KILOGRAMS", "KILOGRAM", "kilogram", "Kilogram", "Kilograms", "kilograms"],
        ["t", "T", "TONS", "TON", "ton", "tons", "Ton", "Tons"]

    ]

    while True:
        response = input(question)
        for item in possible_units:
            if response in item:
                return item[0]

        else:
            print("Sorry, that unit is not valid in this program")



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
        else:
            print(f"Sorry, '{from_unit} is not a valid unit.")


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
# Ask Users For Conversion Type (distance / time / mass)
def num_check(question):

    error = "Please enter a number that is more than zero.\n"

    while True:

        # Ask user for number / exit code
        response = input(question)
        if response == "xxx":
            return "xxx"

        try:
            # ask the user to enter a number
            response = float(response)

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


while True:

    # Ask the user for the amount.
    amount = num_check("\nEnter the amount you want to convert (or 'xxx' to exit): ")

    # Exit Code
    if amount == "xxx":
        break
calculation_to_seconds = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("your entered a negative number, please enter a valid postive number")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\n")
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()
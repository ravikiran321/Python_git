calculation_to_units = 24
name_of_units = "Hours"


def days_to_units(num_of_days):
    condition_check = num_of_days > 0
    print(type(condition_check))
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    try:
        user_input_num = int(user_input)
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            print("you have entered a value 0, please enter a valid positive number")
        else:
            print("you have entered negative value , no conversion for you")
    except ValueError:
        print("you have entered invalid input , please enter positive values only")


user_input = input("hai , please enter a number of days and i will convert in to hours!! \n")
validate_and_execute()

calculation_to_units = 24
name_of_units = "Hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
    else:
        return "please enter a positive number"


user_input = input("hai , please enter a number of days and i will convert in to hours!! \n")
user_input_num = int(user_input)
calculated_value = days_to_units(user_input_num)
print(calculated_value)  #provided the space

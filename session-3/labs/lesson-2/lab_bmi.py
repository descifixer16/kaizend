# 2.3 Using Functions in Scripts

#     Calculate for users Body Mass Index(BMI).
#     There are 2 ways of calculating BMI, metric and Imperial.
#     We will calculate using metric formulation.

#     Formula:
#         BMI = (weight in kg / height in meters squared ) 
#         For Imperial systems, it’s formula is that weight is in pounds and height is in inches then you multiply the result by 703.
#         BMI = [Weight (lbs) / Height (inches)²] x 703

#     Procedure:
#         - prompt the user for their information.
#         - gather the results
#         - make the calculations
#         - If we can’t understand the measurement system, then we need to prompt the user again after
#             explaining the error.

def gather_info():
    """ 
        Gather information from user inputs.
        weight, height and system of measurement
    """

    weight = float(input("What is your weight? ( pounds or kilograms ): "))
    height = float(input("What is your height? ( inches or meters ): "))
    system = input("Are your measurements in metric or imperial units?: ").lower().strip()

    return (weight, height, system)

# print(gather_info())  # ==> (25.0, 25.0, 'metric')

def calc_bmi(weight, height, system="metric"):
    """ 
        Process/Calculate gathered information from a users inputs.
        Return Body Mass Index from the gathered informations.
    """

    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
        
    return bmi



while True:
    try:
        weight, height, system = gather_info()
        if system.startswith('i'):
            bmi = calc_bmi(weight, system='imperial', height=height)
            print(f"Your BMI is {bmi}")
            break
        elif system.startswith('m'):
            bmi = calc_bmi(weight, height)
            print(f"Your BMI is {bmi}")
            break
        else:
            print("Error: Unknown measurement system. Please use imperial or metric.")
    except ValueError:
        print('Please enter integers only')

    
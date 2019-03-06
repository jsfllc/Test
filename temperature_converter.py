"""
This program takes a temperature value from a user and converts that temperature to either
Celsius or Fahrenheit based upon the choice of the user.
"""


def temperature_converter():

    start_temp = float(input("Enter a temperature: "))

    while True:
        convert = input("Would you like to convert that to (C)elsius or (F)ahrenheit?: ").lower()

        if convert == "c":
            celsius = (5/9) * (start_temp - 32)
            print("\nThe temperature in Celsius is: " + str(round(celsius, 2)) + " degrees.")
            break

        elif convert == "f":
            fahrenheit = (start_temp * 9/5) + 32
            print("\nThe temperature in Fahrenheit is: " + str(round(fahrenheit, 2)) + " degrees.")
            break

        else:
            print("\nPlease enter either F for Fahrenheit or C for Celsius.")


if __name__ == '__main__':
    temperature_converter()

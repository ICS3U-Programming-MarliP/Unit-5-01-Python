#!usr/bin/env python3
# Created By: Marli Peters
# Date: Nov. 18, 2023
# This program creates a function that asks user for the temperature
# in celsius then converts it into fahrenheit and displays it for them.


def temp_convert():
    # get temperature in celsius as string

    temp_c_str = str(input("Enter temperature in celsius: "))

    # catch input errors

    try:
        temp_c_float = float(temp_c_str)

    except Exception:
        print("Please enter a valid temperature.")

    # calculate temperature in fahrenheit

    else:
        temp_f = (9 / 5) * temp_c_float + 32

        # display temperature in fahrenheit

        print("The temperature in fahrenheit is {:.3}".format(temp_f))


def main():
    # call temp convert function

    temp_convert()


if __name__ == "__main__":
    main()

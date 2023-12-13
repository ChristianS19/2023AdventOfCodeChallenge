"""
Calibration numbvaluesers have been incorrectly stored for targeting the trebuchet. On each line, the calibration value can 
be found by combining the first digit and the last digit (in that order) of the characters to form a single two-digit number. 

Consider your entire calibration document. What is the sum of all of the calibration values?

Mixed up calibration values can be found at "https://adventofcode.com/2023/day/1/input"
# Calibration values have been saved locally rather than fetched during the code.
"""
def calibration_values(input):
    """
    Takes in a text file, and returns the sum of the combined first and last digit of each line in the file (e.g. a1bcd34r = 14)
    input: str, the location of the input file.

    Returns the sum of all calibration values as an integer.
    """
    calibration_sum = 0
    with open(input, 'r') as file:
        for line in file:
            digits = [s for s in line if s.isdigit()]
            first_num = digits[0]
            second_num = digits[-1]
            calibration_sum += int(first_num + second_num)
    file.close()
    return calibration_sum


if __name__ == '__main__':
    main()